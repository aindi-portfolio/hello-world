// router.jsx
import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage"
import Characters from "./pages/Characters";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        index: true,
        element: <HomePage />
      },
      {
        path: "/characters",
        element: <Characters />
      }
    ],
  },
  {
    path: "*",
    ErrorBoundary: () => <div>Something went wrong!</div>,
  }
]);

export default router;



//// When you come back, add more coponents to the homepage, like a footer and a list of characters.