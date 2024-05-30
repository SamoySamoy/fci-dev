import { useNavigate } from "react-router-dom";

interface Book {
  id: number;
  title: string;
  author: string;
  price: string;
  date: string;
}
const Book = ({
  book,
  handleRemoveBook,
}: {
  book: Book;
  handleRemoveBook: (id: number) => void;
}) => {
  const navigate = useNavigate();
  const { id, title, author, price, date } = book;

  return (
    <div className="book">
      <h2>{title}</h2>
      <div className="bookDetail">
        <p>Author: {author}</p>
        <p>Price: {price}</p>
        <p>Date: {date}</p>
      </div>
      <div className="buttons">
        <button onClick={() => navigate(`/edit/${id}`)}>Edit</button>
        <button onClick={() => handleRemoveBook(id)}>Delete</button>
      </div>
    </div>
  );
};

export default Book;
