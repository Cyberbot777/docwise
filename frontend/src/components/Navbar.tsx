import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white px-6 py-4 flex gap-6 items-center">
      <Link to="/" className="hover:underline">Home</Link>
      <Link to="/login" className="hover:underline">Login</Link>
      <Link to="/register" className="hover:underline">Register</Link>
      <Link to="/dashboard" className="hover:underline">Dashboard</Link>
    </nav>
  );
}
