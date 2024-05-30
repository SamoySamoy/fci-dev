import { useNavigate } from "react-router-dom";
import BookForm from "components/form/BookForm";
import { bookApi } from "api/bookApi";

const AddBook = () => {
  const navigate = useNavigate();

  interface CreateBook {
    title: string;
    author: string;
    price: string;
  }

  const handleOnSubmit = async (book: CreateBook) => {
    try {
      await bookApi.createBook(book);
      navigate("/");
    } catch (error) {
      console.error("Error creating book:", error);
    }
  };

  return (
    <div className="addForm">
      <BookForm handleSubmit={handleOnSubmit} />
    </div>
  );
};

export default AddBook;
