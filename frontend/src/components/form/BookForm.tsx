import { useState, ChangeEvent, FormEvent } from "react";

interface CreateBook {
  title: string;
  author: string;
  price: string;
}

interface BookFormProps {
  book?: any;
  handleSubmit: (book: CreateBook & { date: string }) => void;
}

const BookForm = ({ book, handleSubmit }: BookFormProps) => {
  const [bookState, setBookState] = useState<CreateBook>({
    title: book ? book.title : "",
    author: book ? book.author : "",
    price: book ? book.price : "",
  });

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setBookState({
      ...bookState,
      [name]: value,
    });
  };

  const onSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    handleSubmit({
      date: new Date().toDateString(),
      ...bookState,
    });
    if (!book) {
      setBookState({ title: "", author: "", price: "" }); // Only reset if it's a new book
    }
  };

  const renderInputField = (
    label: string,
    placeholder: string,
    name: keyof CreateBook
  ) => (
    <div className="inputField">
      <label>{label}</label>
      <input
        value={bookState[name]}
        onChange={handleChange}
        name={name}
        type="text"
        placeholder={placeholder}
      />
    </div>
  );

  const disabledSubmit =
    !bookState.title || !bookState.author || !bookState.price;

  return (
    <form onSubmit={onSubmit} className="form">
      {renderInputField("Book Name", "Enter name of book...", "title")}
      {renderInputField("Book Author", "Enter name of author...", "author")}
      {renderInputField("Book Price", "Enter price of book...", "price")}
      <button type="submit" className="btnForm" disabled={disabledSubmit}>
        {book ? "Update" : "Submit"}
      </button>
    </form>
  );
};

export default BookForm;
