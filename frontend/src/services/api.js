import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

export const matchResume = (formData) => {
  return API.post("/analyze", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
};
