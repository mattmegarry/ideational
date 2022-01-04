const openRequest = (path, method, body) => {
  const url = "http://localhost:8000/api";

  const options = {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
    body: JSON.stringify(body),
  };

  return fetch(url + path, options)
    .then(async (res) => {
      const result = {};
      result.status = res.status;
      result.data = await res.json();
      return result;
    })
    .catch((err) => console.log("Error:", err));
};

const authRequest = (path, method, body) => {
  const url = "http://localhost:8000/api";

  const options = {
    method: method,
    headers: {
      "Content-Type": "application/json",
      authorization: `Bearer ${localStorage.getItem("token")}`,
    },
    credentials: "include",
    body: JSON.stringify(body),
  };

  return fetch(url + path, options)
    .then(async (res) => {
      const result = {};
      result.status = res.status;
      result.data = await res.json();
      return result;

      if (res.status === 401) {
        localStorage.removeItem("token");
        window.location.href = "/";
      }

      return result;
    })
    .catch((err) => console.log("Error:", err));
};
