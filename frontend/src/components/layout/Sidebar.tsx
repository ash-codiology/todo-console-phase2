import React from 'react';
import { useRouter } from 'next/router';

interface SidebarProps {
  user?: { id: string; email: string };
}

const Sidebar: React.FC<SidebarProps> = ({ user }) => {
  const router = useRouter();

  const navItems = [
    { name: 'Dashboard', path: '/dashboard', icon: 'M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6' },
    { name: 'Create Task', path: '/dashboard/create', icon: 'M12 6v6m0 0v6m0-6h6m-6 0H6' },
  ];

  return (
    <div className="w-64 bg-gradient-to-b from-yellow-300 to-yellow-600 text-white shadow-xl h-full flex-shrink-0">
      <div className="p-5 border-b border-yellow-500/30">
        <div className="flex items-center space-x-3">
          <div className="bg-white/20 p-2 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 002 2h2a2 2 0 002-2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
            </svg>
          </div>
          <h2 className="text-xl font-bold">TodoPro</h2>
        </div>
        {user && (
          <div className="mt-4 p-3 bg-white/10 rounded-lg">
            <p className="text-sm font-medium truncate">{user.email.split('@')[0]}</p>
            <p className="text-xs text-yellow-600 truncate">{user.email}</p>
          </div>
        )}
      </div>
      <nav className="mt-6">
        <ul>
          {navItems.map((item) => (
            <li key={item.name}>
              <button
                onClick={() => router.push(item.path)}
                className={`w-full text-left px-6 py-4 text-sm font-medium transition-all duration-200 flex items-center space-x-3 ${
                  router.pathname === item.path
                    ? 'bg-white/20 text-white border-l-4 border-white'
                    : 'text-yellow-800 hover:bg-white/10 hover:text-white'
                }`}
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d={item.icon} />
                </svg>
                <span>{item.name}</span>
              </button>
            </li>
          ))}
        </ul>
      </nav>
      <div className="absolute bottom-0 w-64 p-4 bg-gradient-to-t text-yellow-700 to-transparent">
        <div className="text-xs text-yellow-300 text-center">
          Secure & Organized
        </div>
      </div>
    </div>
  );
};

export default Sidebar;