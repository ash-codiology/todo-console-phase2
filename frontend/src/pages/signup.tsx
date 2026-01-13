import React from 'react';
import SignupForm from '../components/auth/SignupForm';
import { useRouter } from 'next/router';

const SignupPage: React.FC = () => {
  const router = useRouter();

  const switchToSignin = () => {
    router.push('/signin');
  };

  return (
    <div className="min-h-screen bg-teal-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="text-center">
          <div className="mx-auto flex justify-center">
            <div className="bg-gradient-to-r from-teal-600 to-teal-700 p-3 rounded-2xl shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
              </svg>
            </div>
          </div>
          <h1 className="mt-6 text-3xl font-light text-gray-800">
            TodoPro
          </h1>
          <p className="mt-2 text-gray-600">
            Sign up to get started managing your tasks
          </p>
        </div>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white/70 backdrop-blur-sm shadow-sm rounded-2xl p-8 border border-teal-100">
          <SignupForm onSwitchToSignin={switchToSignin} />
        </div>
      </div>
    </div>
  );
};

export default SignupPage;