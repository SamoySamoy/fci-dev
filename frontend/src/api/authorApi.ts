// src/api/authorApi.ts
import { apiClient } from "./apiClient";

export const authorApi = {
  getAllAuthors: async () => {
    return apiClient.get("http://localhost:8080/authors/");
  },
  getAuthorById: async (id: number) => {
    return apiClient.get(`http://localhost:8080/authors/${id}`);
  },
  createAuthor: async (author: any) => {
    return apiClient.post("http://localhost:8080/authors/", author);
  },
  updateAuthor: async (id: number, author: any) => {
    return apiClient.put(`http://localhost:8080/authors/${id}`, author);
  },
  deleteAuthor: async (id: number) => {
    return apiClient.delete(`http://localhost:8080/authors/${id}`);
  },
};
