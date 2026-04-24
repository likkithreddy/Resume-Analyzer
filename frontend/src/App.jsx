import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Upload from "./pages/Upload";
import Dashboard from "./pages/Dashboard";
import Recommendations from "./pages/Recommendations";
import Simulation from "./pages/Simulation";


function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/upload" element={<Upload />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/recommendations" element={<Recommendations />} />
      <Route path="/simulation" element={<Simulation />} />

    </Routes>
  );
}

export default App;
