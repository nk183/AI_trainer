from crypt import methods
import ExercisesModule as trainer
import AudioCommSys as audio_sys

from flask import Flask, render_template, Response, request, redirect, url_for
from camera import VideoCamera
import time


app = Flask(__name__, static_folder='static', template_folder="template")


user_first_name = ""
difficulty_level = ""
age = ""
weight = ""
gender = ""
calories = "0"
user_email = ""


@app.route("/trainer", methods=["GET", "POST"])
def index():
    global difficulty_level
    global age
    global weight
    global gender
    # global calories

    user_first_name = "Chisom"
    difficulty_level = request.form["gridRadiosDifficulty"]
    age = request.form["gridRadiosAge"]
    weight = request.form["numberInputWeight"]
    gender = request.form["gridRadiosGender"]

    print(user_first_name, difficulty_level, age, weight, gender)
    return render_template(
        "/index.html",
        user_first_name=user_first_name,
        difficulty_level=request.form["gridRadiosDifficulty"],
        calories=calories,
        user_email=user_email,

    )

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("/preference.html")

@app.route("/preferencepage", methods=["GET", "POST"])
def set_up():
    if request.method=='POST':
        global user_first_name
        global user_email
    
        user_first_name = request.form["name"]
        email = request.form["email"]
        print(user_first_name, email)
        # return redirect(url_for('home'))
    return render_template("preference.html")  


# For real world.
def gen_camera(camera):
    while True:
        frame = camera.get_frame()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n\r\n")


@app.route("/video_feed_camera", methods=["GET", "POST"])
def video_feed_camera():
    return Response(
        gen_camera(VideoCamera()), mimetype="multipart/x-mixed-replace; boundary=frame"
    )

# For Test
def gen():
    calories = 0
    start = time.process_time()
    time_elapsed_for_round = 0

    for i in range(0, 5):
        difficulty_level_map = {"Easy": 1, "Intermediate": 2, "Hard": 3}
        level = difficulty_level_map[difficulty_level]
        print(level)
        print("xxxttttttttttttt",trainer)
        for i in trainer.start_workout_session(level).complete_path(
            difficulty_level, age, weight, gender
        ):
            yield i
            print("hereee ------------------------------------")

            time_elapsed_for_round = int(time.process_time() - start)
            print(time_elapsed_for_round)
            calories = trainer.start_workout_session(level).calculate_calories(
                time_elapsed_for_round, weight, gender
            )

            # with app.app_context():
            #     sse.publish(
            #         {"calorie": round(calories / 2, 2), "time": time_elapsed_for_round},
            #         type="calorie",
            #     )
            print(time_elapsed_for_round, calories)
        print("DONE!")
    
    for i in  trainer.start_workout_session().completion_screen("TrainerImages/you_rock.jpeg"):
        yield i
        audio_sys.text_to_speech(
                "Workout complete! You will recieve your stats in your email! You, did it."
            )
        break
    # email_sys.email_user(
    #         "okwor@gmail.com", "Chisom Okwor", str(round(calories / 2, 2)), time_elapsed_for_round
    #     )

@app.route("/video_feed")
def video_feed():
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


# -----------
def main():
    audio_sys.text_to_speech("Are you a registered user? (Enter YES or NO)")


    audio_sys.text_to_speech("Hello " + first_name + ". Select a difficulty Level: Easy, Medium or Hard.")
    difficulty_level = int(input("For easy enter 1, for medium 2, and for hard 3: "))

    audio_sys.text_to_speech("When you are ready, say READY.")
    ready = (audio_sys.speech_to_text()).lower()

    if "ready" in ready:
        session = trainer.start_workout_session(difficulty_level)
        performance = session.complete_path()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
    main()
