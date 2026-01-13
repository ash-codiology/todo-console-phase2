import React, { useState, useEffect, createContext, useContext } from 'react';
import { apiService } from '../services/api';

interface User {
  id: string;
  email: string;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  signIn: (email: string, password: string) => Promise<void>;
  signUp: (email: string, password: string) => Promise<void>;
  signOut: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: React.ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // Check if user is logged in on initial load
  useEffect(() => {
    const token = localStorage.getItem('access_token');
    const storedUser = localStorage.getItem('user');

    if (token && storedUser) {
      apiService.setToken(token);
      setUser(JSON.parse(storedUser));
    }
    setLoading(false);
  }, []);

  const signIn = async (email: string, password: string) => {
    try {
      const response: any = await apiService.signin(email, password);

      if (response.access_token) {
        // Store the token and user info
        localStorage.setItem('access_token', response.access_token);
        localStorage.setItem('user', JSON.stringify({ id: response.user_id, email }));
        apiService.setToken(response.access_token);

        setUser({ id: response.user_id, email });
      }
    } catch (error) {
      console.error('Sign in failed:', error);
      throw error;
    }
  };

  const signUp = async (email: string, password: string) => {
    try {
      const response: any = await apiService.signup(email, password);

      // Auto-sign in after successful signup
      await signIn(email, password);
    } catch (error) {
      console.error('Sign up failed:', error);
      throw error;
    }
  };

  const signOut = () => {
    setUser(null);
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    apiService.setToken(null);
  };

  const value = {
    user,
    loading,
    signIn,
    signUp,
    signOut
  };

  return React.createElement(
    AuthContext.Provider,
    { value },
    children
  );
};