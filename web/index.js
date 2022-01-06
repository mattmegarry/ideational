const login = async (e) => {
  try {
    const username = document.querySelector("input[type=text]").value;
    const password = document.querySelector("input[type=password]").value;
    const res = await openRequest("/token/obtain/", "POST", {
      username,
      password,
    });
    const { status, data } = res;
    if (status === 200) {
      localStorage.setItem("token", data.access);
      const res = await authRequest("/ideas/picovoice-key/", "GET");
      localStorage.setItem("picovoice", res.data.accessKey);
      await getIdeas();
    } else {
      alert("Invalid Credentials");
    }
  } catch (err) {
    console.log(err);
  }
};

const getIdeas = async () => {
  try {
    const res = await authRequest("/ideas/", "GET");
    const { status, data } = res;
    if (status === 200) {
      renderIdeas(document.getElementById("ideas-list"), data);
    } else {
      alert("Invalid Credentials");
    }
  } catch (err) {
    console.log(err);
  }
};

const renderIdeas = (container, ideas) => {
  container.innerHTML = "";
  ideas.forEach((idea) => {
    const li = document.createElement("li");
    li.innerHTML = idea.idea_text;
    container.appendChild(li);
    if (idea.audio_file) {
      li.appendChild(buildPlayer(idea));
    }
  });
};

const buildPlayer = (idea) => {
  const player = document.createElement("audio");
  const string = idea.audio_file;
  const path = string.substring(0, string.lastIndexOf("/") + 1);
  const name = string.substring(string.lastIndexOf("/") + 1, string.length);
  player.setAttribute("src", path + "converted_" + name);
  player.setAttribute("controls", true);
  return player;
};
