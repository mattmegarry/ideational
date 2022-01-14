const serverUrl = devEnv
  ? "http://localhost:8000/api"
  : "https://ACTUAL SERVER IP.com/api";

const openRequest = (path, method, body) => {
  const options = {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
    body: JSON.stringify(body),
  };

  return fetch(serverUrl + path, options)
    .then(async (res) => {
      const result = {};
      result.status = res.status;
      result.data = await res.json();
      return result;
    })
    .catch((err) => console.log("Error:", err));
};

const authRequest = (path, method, body, nonJsonContentType) => {
  const headers = { authorization: `Bearer ${localStorage.getItem("token")}` };
  let variableBody;

  if (!nonJsonContentType) {
    headers["Content-Type"] = "application/json";
    variableBody = JSON.stringify(body);
  } else {
    // https://stackoverflow.com/a/39281156/14269225
    // Django doesn't like us setting the content type to undefined, but we can just not specify it
    variableBody = body;
    for (var value of variableBody.values()) {
      console.log(value);
    }
  }

  const options = {
    method: method,
    headers: headers,
    credentials: "include",
    body: variableBody,
  };

  return fetch(serverUrl + path, options)
    .then(async (res) => {
      const result = {};
      result.status = res.status;
      result.data = await res.json();

      if (res.status === 401) {
        localStorage.removeItem("token");
        window.location.href = "/";
      }

      return result;
    })
    .catch((err) => console.log("Error:", err));
};
