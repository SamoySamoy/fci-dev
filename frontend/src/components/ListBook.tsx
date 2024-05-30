import { useEffect, useState } from "react";
import Book from "./Book";
import { bookApi } from "api/bookApi";

const ListBook = () => {
  const [books, setBooks] = useState<any[]>([]);
  useEffect(() => {
    fetchAuthors();
  }, []);

  const fetchAuthors = async () => {
    try {
      const response = await bookApi.getAllBooks();
      setBooks(response);
    } catch (error) {
      console.error("Error fetching bookss:", error);
    }
  };

  const handleRemoveBook = async (id: number) => {
    try {
      await bookApi.deleteBook(id);
      fetchAuthors(); // Reload the list of books
    } catch (error) {
      console.error("Error deleting book:", error);
    }
  };

  return (
    <div className="listBook">
      {books.length ? (
        books.map((book) => (
          <Book book={book} key={book.id} handleRemoveBook={handleRemoveBook} />
        ))
      ) : (
        <p className="noData">No books avaliable, Please add some book!</p>
      )}
    </div>
  );
};

export default ListBook;
