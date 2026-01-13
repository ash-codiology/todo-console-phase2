// Base API service for communication with backend

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'https://todo-console-phase2.vercel.app/api';

interface AuthResponse {
  access_token: string;
  token_type: string;
  user_id: string;
}

interface Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

class ApiService {
  private token: string | null = null;

  setToken(token: string | null) {
    this.token = token;
  }

  async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    // Always get the most recent token from localStorage
    const token = localStorage.getItem('token') || localStorage.getItem('access_token');
    if (token) {
      this.token = token; // Update internal token for consistency
    }

    const url = `${API_BASE_URL}${endpoint}`;

    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    } as Record<string, string>;

    if (token) { // Use the token from localStorage directly
      headers['Authorization'] = `Bearer ${token}`;
    }

    const config: RequestInit = {
      headers,
      ...options,
    };

    try {
      const response = await fetch(url, config);

      if (!response.ok) {
        // If we get a 401 Unauthorized, try to refresh the token from localStorage and retry
        if (response.status === 401) {
          const newToken = localStorage.getItem('token') || localStorage.getItem('access_token');
          if (newToken && newToken !== token) { // Compare with the token used in this request
            this.token = newToken;
            headers['Authorization'] = `Bearer ${newToken}`;

            // Retry the request with the new token
            const retryResponse = await fetch(url, { ...config, headers });

            if (!retryResponse.ok) {
              const errorData = await retryResponse.json().catch(() => ({}));
              throw new Error(errorData.detail || `HTTP error! status: ${retryResponse.status}`);
            }

            return await retryResponse.json();
          }
        }

        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.error(`API request failed: ${endpoint}`, error);
      throw error;
    }
  }

  // Auth methods
  async signup(email: string, password: string): Promise<AuthResponse> {
    return this.request<AuthResponse>('/auth/signup', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  }

  async signin(email: string, password: string): Promise<AuthResponse> {
    const response = await this.request<AuthResponse>('/auth/signin', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });

    // Store the token if returned by the backend
    if (response.access_token) {
      this.setToken(response.access_token);
    }

    return response;
  }

  // Todo methods
  async getTodos(): Promise<Todo[]> {
    return this.request<Todo[]>('/todos');
  }

  async getTodo(id: string): Promise<Todo> {
    return this.request<Todo>(`/todos/${id}`);
  }

  async createTodo(title: string, description?: string): Promise<Todo> {
    return this.request<Todo>('/todos', {
      method: 'POST',
      body: JSON.stringify({ title, description }),
    });
  }

  async updateTodo(id: string, title?: string, description?: string, completed?: boolean): Promise<Todo> {
    return this.request<Todo>(`/todos/${id}`, {
      method: 'PUT',
      body: JSON.stringify({ title, description, completed }),
    });
  }

  async deleteTodo(id: string): Promise<void> {
    return this.request<void>(`/todos/${id}`, {
      method: 'DELETE',
    });
  }

  async toggleTodoCompletion(id: string): Promise<Todo> {
    return this.request<Todo>(`/todos/${id}/toggle`, {
      method: 'PATCH',
    });
  }
}

export const apiService = new ApiService();