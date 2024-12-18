import React from 'react';
import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from '../../contexts/auth-context';

const ProtectedRoute = () => {
  const auth = useAuth();

  if (!auth.loggedIn) return <Navigate to="/signin" />;
    return <Outlet />;

}
export default ProtectedRoute;