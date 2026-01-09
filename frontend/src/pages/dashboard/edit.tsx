import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { useAuth } from '../../hooks/useAuth';
import Sidebar from '../../components/layout/Sidebar';
import { apiService } from '../../services/api';

interface Todo {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
  updated_at: string;
}

const EditTaskPage: React.FC = () => {
  const router = useRouter();
  const { user, loading } = useAuth();
  const { id } = router.query;
  const [todo, setTodo] = useState<Todo | null>(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [completed, setCompleted] = useState(false);
  const [error, setError] = useState('');
  const [loadingTodo, setLoadingTodo] = useState(true);
  const [loadingSubmit, setLoadingSubmit] = useState(false);

  useEffect(() => {
    if (!loading && !user) {
      router.push('/signin');
      return;
    }
    if (user && id) {
      // Ensure token is available before fetching
      const token = localStorage.getItem('token') || localStorage.getItem('access_token');
      if (token) {
        apiService.setToken(token);
      }

      // Handle the case where id might be an array
      const todoId = Array.isArray(id) ? id[0] : id;
      fetchTodo(todoId);
    }
  }, [user, loading, id, router]);

  const fetchTodo = async (todoId?: string) => {
    try {
      setLoadingTodo(true);
      // Ensure the token is loaded from localStorage
      // Check both possible token storage keys for compatibility
      const token = localStorage.getItem('token') || localStorage.getItem('access_token');
      if (token) {
        apiService.setToken(token);
      }

      // Use the passed todoId or fallback to the router query id
      const taskId = todoId || (Array.isArray(id) ? id[0] : id as string);

      if (!taskId) {
        setError('Task ID is missing');
        return;
      }

      const response = await apiService.getTodo(taskId);
      setTodo(response);
      setTitle(response.title);
      setDescription(response.description || '');
      setCompleted(response.completed);
    } catch (err) {
      setError('Failed to load task');
      console.error('Failed to fetch todo:', err);
    } finally {
      setLoadingTodo(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    // Ensure token is available before proceeding
    const token = localStorage.getItem('token') || localStorage.getItem('access_token');
    if (!token) {
      setError('Authentication token not found. Please sign in again.');
      return;
    }
    apiService.setToken(token);

    // Get the correct task ID (handling potential array from router query)
    const taskId = Array.isArray(id) ? id[0] : id as string;

    if (!taskId) {
      setError('Task ID is missing');
      return;
    }

    setLoadingSubmit(true);
    setError('');

    try {
      await apiService.request(`/todos/${taskId}`, {
        method: 'PUT',
        body: JSON.stringify({ title, description, completed }),
      });
      router.push('/dashboard');
    } catch (err: any) {
      setError(err.message || 'Failed to update task');
      console.error('Failed to update task:', err);
    } finally {
      setLoadingSubmit(false);
    }
  };

  if (loading || loadingTodo) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
          <p className="text-gray-600 mt-2">Loading...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return null;
  }

  if (!todo && !loadingTodo && error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-red-600">Error: {error}</p>
          <button
            onClick={() => router.back()}
            className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Go Back
          </button>
        </div>
      </div>
    );
  }

  if (!todo) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-600">Task not found</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen bg-gradient-to-br from-yellow-50 to-yellow-100">
      <Sidebar user={user} />
      <div className="flex-1 flex flex-col overflow-hidden">
        <main className="flex-1 overflow-y-auto p-6">
          <div className="max-w-2xl mx-auto">
            <div className="mb-8">
              <h1 className="text-3xl font-bold text-gray-900">Edit Task</h1>
              <p className="text-gray-600 mt-2">Update your task details</p>
            </div>

            <div className="bg-white rounded-xl shadow-lg border border-gray-200 p-8">
              {error && (
                <div className="mb-6 bg-red-50 border-l-4 border-red-500 p-4 rounded-lg">
                  <div className="flex">
                    <div className="flex-shrink-0">
                      <svg className="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                      </svg>
                    </div>
                    <div className="ml-3">
                      <p className="text-sm text-red-700">
                        {error}
                      </p>
                    </div>
                  </div>
                </div>
              )}

              <form onSubmit={handleSubmit}>
                <div className="mb-8">
                  <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-2">
                    Task Title *
                  </label>
                  <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500 transition duration-200"
                    placeholder="What needs to be done?"
                    required
                  />
                </div>

                <div className="mb-8">
                  <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-2">
                    Description (Optional)
                  </label>
                  <textarea
                    id="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    rows={5}
                    className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-yellow-500 focus:border-yellow-500 transition duration-200"
                    placeholder="Add more details about this task..."
                  />
                </div>

                <div className="mb-8 flex items-center">
                  <input
                    type="checkbox"
                    id="completed"
                    checked={completed}
                    onChange={(e) => setCompleted(e.target.checked)}
                    className="h-5 w-5 text-yellow-600 rounded focus:ring-yellow-500"
                  />
                  <label htmlFor="completed" className="ml-2 block text-sm text-gray-700">
                    Mark as completed
                  </label>
                </div>

                <div className="flex items-center justify-between space-x-4">
                  <button
                    type="button"
                    onClick={() => router.push('/dashboard')}
                    className="px-6 py-3 text-sm font-medium text-gray-700 bg-gray-200 rounded-lg hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500 transition duration-200"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={loadingSubmit}
                    className="px-6 py-3 text-sm font-medium text-white bg-gradient-to-r from-yellow-500 to-yellow-600 rounded-lg hover:from-yellow-600 hover:to-yellow-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-yellow-500 disabled:opacity-50 transition-all duration-200 hover:scale-105 shadow-md"
                  >
                    {loadingSubmit ? (
                      <span className="flex items-center">
                        <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                        Updating...
                      </span>
                    ) : (
                      <span className="flex items-center">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2V7a2 2 0 00-2-2h-2m-5 0V4a1 1 0 011-1h2a1 1 0 011 1v3M4 7h16" />
                        </svg>
                        Update Task
                      </span>
                    )}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </main>

        {/* Footer */}
        <footer className="py-4 bg-gradient-to-r from-yellow-600 to-yellow-700 text-white text-center text-sm">
          <div className="container mx-auto">
            <p>All rights to tabsheera shakeel</p>
          </div>
        </footer>
      </div>
    </div>
  );
};

export default EditTaskPage;