from PIL import Image
import os

def detect_deepfake(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
        width, height = img.size

        # Basic image analysis
        pixels = list(img.getdata())

        # Average RGB values
        total_r = sum(p[0] for p in pixels)
        total_g = sum(p[1] for p in pixels)
        total_b = sum(p[2] for p in pixels)

        total = len(pixels)

        avg_r = total_r / total
        avg_g = total_g / total
        avg_b = total_b / total

        print("\nImage Analysis")
        print("----------------")
        print("Width :", width)
        print("Height:", height)
        print("Average Red  :", round(avg_r, 2))
        print("Average Green:", round(avg_g, 2))
        print("Average Blue :", round(avg_b, 2))

        # Demo heuristic
        score = 0

        if width == height:
            score += 1

        if max(avg_r, avg_g, avg_b) - min(avg_r, avg_g, avg_b) < 15:
            score += 1

        print("\nDetection Result")
        print("----------------")

        if score >= 2:
            print("⚠ Image may require further deepfake analysis.")
        else:
            print("✓ Image does not show these basic warning signs.")

        print("\nNote: This is an educational prototype.")
        print("It is NOT a reliable real-world deepfake detector.")

    except FileNotFoundError:
        print("Image file not found.")
    except Exception as e:
        print("Error:", e)


image_path = input("Enter image path: ")
detect_deepfake(image_path)
