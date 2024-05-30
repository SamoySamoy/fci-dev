import { useNavigate, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import BookForm from "./form/BookForm";
import { bookApi } from "api/bookApi";

const EditBook = () => {
  const { id } = useParams();
  const [bookToEdit, setBookToEdit] = useState<any>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchBook = async () => {
      if (id) {
        const book = await bookApi.getBookById(parseInt(id));
        setBookToEdit(book);
      }
    };
    fetchBook();
  }, [id]);

  const handleOnSubmit = async (book: any) => {
    if (id) {
      await bookApi.updateBook(parseInt(id), book);
      navigate("/");
    }
  };

  if (!bookToEdit) {
    return <div>Loading...</div>;
  }

  return (
    <div className="addForm">
      <BookForm book={bookToEdit} handleSubmit={handleOnSubmit} />
    </div>
  );
};

export default EditBook;
