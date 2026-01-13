import React from 'react';
import SigninForm from '../components/auth/SigninForm';
import { useRouter } from 'next/router';

const SigninPage: React.FC = () => {
  const router = useRouter();

  const switchToSignup = () => {
    router.push('/signup');
  };

  return (
    <div className="min-h-screen bg-teal-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="text-center">
          <div className="mx-auto flex justify-center">
            <div className="bg-gradient-to-r from-teal-600 to-teal-700 p-3 rounded-2xl shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 002 2h2a2 2 0 002-2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
              </svg>
            </div>
          </div>
          <h1 className="mt-6 text-3xl font-light text-gray-800">
            TodoPro
          </h1>
          <p className="mt-2 text-gray-600">
            Sign in to your account
          </p>
        </div>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white/70 backdrop-blur-sm shadow-sm rounded-2xl p-8 border border-teal-100">
          <SigninForm onSwitchToSignup={switchToSignup} />
        </div>
      </div>
    </div>
  );
};

export default SigninPage;