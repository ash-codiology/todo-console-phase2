// Base API service for communication with backend

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

interface ApiResponse<T> {
  data: T;
  success: boolean;
}

class ApiService {
  private token: string | null = null;

  setToken(token: string | null) {
    this.token = token;
  }

  async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    // Ensure we have a token, if not try to retrieve it from localStorage
    if (!this.token) {
      const token = localStorage.getItem('token') || localStorage.getItem('access_token');
      if (token) {
        this.token = token;
      }
    }

    const url = `${API_BASE_URL}${endpoint}`;

    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    } as Record<string, string>;

    if (this.token) {
      headers['Authorization'] = `Bearer ${this.token}`;
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
          if (newToken && newToken !== this.token) {
            this.token = newToken;
            headers['Authorization'] = `Bearer ${this.token}`;

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
  async signup(email: string, password: string) {
    return this.request('/auth/signup', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  }

  async signin(email: string, password: string) {
    const response = await this.request('/auth/signin', {
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
  async getTodos() {
    return this.request('/todos');
  }

  async getTodo(id: string) {
    return this.request(`/todos/${id}`);
  }

  async createTodo(title: string, description?: string) {
    return this.request('/todos', {
      method: 'POST',
      body: JSON.stringify({ title, description }),
    });
  }

  async updateTodo(id: string, title?: string, description?: string, completed?: boolean) {
    return this.request(`/todos/${id}`, {
      method: 'PUT',
      body: JSON.stringify({ title, description, completed }),
    });
  }

  async deleteTodo(id: string) {
    return this.request(`/todos/${id}`, {
      method: 'DELETE',
    });
  }

  async toggleTodoCompletion(id: string) {
    return this.request(`/todos/${id}/toggle`, {
      method: 'PATCH',
    });
  }
}

export const apiService = new ApiService();