// router.jsx
import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage"
import Characters from "./pages/Characters";
import Locations from "./pages/Locations";
import Episodes from "./pages/Episodes";
import About from "./pages/About";

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
      },
      {
        path: "/locations",
        element: <Locations />
      },
      {
        path: "/episodes",
        element: <Episodes />
      },
      {
        path: "/about",
        element: <About />
      }
    ]
  },
  {
    path: "*",
    element: <div>404 Not Found</div>
  }
]);

export default router;