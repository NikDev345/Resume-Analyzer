import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect } from "react";
import Home from "./components/Home";
import ResumeAnalyzer from "./components/ResumeAnalyzer";

function App() {
  useEffect(() => {
    const move = (e) => {
      document.documentElement.style.setProperty("--x", `${e.clientX}px`);
      document.documentElement.style.setProperty("--y", `${e.clientY}px`);
    };
    window.addEventListener("mousemove", move);
    return () => window.removeEventListener("mousemove", move);
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/analyze" element={<ResumeAnalyzer />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
