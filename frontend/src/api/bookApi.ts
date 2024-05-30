// src/api/bookApi.ts
import { apiClient } from "./apiClient";

export const bookApi = {
  getAllBooks: async () => {
    return apiClient.get("http://localhost:8080/books/");
  },
  getBookById: async (id: number) => {
    return apiClient.get(`http://localhost:8080/books/${id}`);
  },
  createBook: async (book: any) => {
    return apiClient.post("http://localhost:8080/books/", book);
  },
  updateBook: async (id: number, book: any) => {
    return apiClient.put(`http://localhost:8080/books/${id}`, book);
  },
  deleteBook: async (id: number) => {
    return apiClient.delete(`http://localhost:8080/books/${id}`);
  },
};
