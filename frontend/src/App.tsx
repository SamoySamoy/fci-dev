import { Route, Routes } from "react-router-dom";
import "./App.css";
import AddBook from "components/AddBook";
import EditBook from "components/EditBook";
import Header from "components/Header";
import ListBook from "components/ListBook";

function App() {
  return (
    <div className="container">
      <Header />
      <Routes>
        <Route path="/" element={<ListBook />} />
        <Route path="/add" element={<AddBook />} />
        <Route path="/edit/:id" element={<EditBook />} />
      </Routes>
    </div>
  );
}

export default App;
