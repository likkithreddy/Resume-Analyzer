import { createContext, useState } from "react";

export const ResultContext = createContext();

export const ResultProvider = ({ children }) => {
  const [result, setResult] = useState(null);

  return (
    <ResultContext.Provider value={{ result, setResult }}>
      {children}
    </ResultContext.Provider>
  );
};
