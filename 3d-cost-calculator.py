# import necessary libraries
import streamlit as st
from fpdf import FPDF
import base64

# Define the Streamlit app
def main():
    # Set the title and description
    st.title("3D Model Cost Estimator")
    st.write("Estimate the cost of your 3D modeling project")

    # User inputs
    st.sidebar.header("Project Details")
    dimensions = st.sidebar.slider("Select Project Dimensions (in cm)", 1, 100, (10, 10))
    material = st.sidebar.selectbox("Select Material", ["Plastic", "Metal", "Wood"])
    complexity = st.sidebar.slider("Select Project Complexity", 1, 10, 5)

    # Calculate estimated cost and recommendations
    estimated_cost, cost_breakdown = calculate_cost(dimensions, material, complexity)
    recommendations = generate_recommendations(complexity)

    # Display project summary
    st.header("Project Summary")
    st.write("Here's a summary of your project:")
    st.write(f"- Dimensions: {dimensions[0]} cm x {dimensions[1]} cm")
    st.write(f"- Material: {material}")
    st.write(f"- Complexity: {complexity} (1 = Simple, 10 = Complex)")

    # Display the estimated cost
    st.header("Estimated Cost")
    st.subheader(f"The estimated cost for your project is $ {estimated_cost:.2f}")

    # Display detailed cost breakdown
    st.header("Cost Breakdown")
    st.write("Here's the breakdown of the estimated cost:")
    st.write(f"- Base Cost: $ {cost_breakdown['base_cost']:.2f}")
    st.write(f"- Material Cost: $ {cost_breakdown['material_cost']:.2f}")
    st.write(f"- Complexity Cost: $ {cost_breakdown['complexity_cost']:.2f}")

    # Display cost-saving tips
    st.header("Cost-Saving Tips")
    if recommendations:
        st.write("To reduce costs and optimize your project, consider the following tips:")
        for i, recommendation in enumerate(recommendations, 1):
            st.write(f"{i}. {recommendation}")
    else:
        st.write("No specific recommendations for the selected complexity.")

    # Add a "Download Report" button
    download_report_as_pdf(dimensions, material, complexity, estimated_cost, cost_breakdown, recommendations)

# Function to calculate the estimated cost (same as previous code)
def calculate_cost(dimensions, material, complexity):
    # Placeholder values for cost components (replace with real pricing data)
    base_cost_per_sq_cm = 0.05  # Placeholder base cost per sq. cm
    material_cost_multiplier = {"Plastic": 1.0, "Metal": 1.5, "Wood": 1.2}  # Placeholder multipliers

    # Calculate base cost
    base_cost = dimensions[0] * dimensions[1] * base_cost_per_sq_cm

    # Calculate material cost
    material_cost = base_cost * material_cost_multiplier.get(material, 1.0)

    # Calculate complexity cost (adjust the formula as needed)
    complexity_cost = base_cost * (complexity / 5.0)

    # Calculate total cost
    total_cost = base_cost + material_cost + complexity_cost

    # Create a breakdown of cost components
    cost_breakdown = {
        "base_cost": base_cost,
        "material_cost": material_cost,
        "complexity_cost": complexity_cost,
    }

    return total_cost, cost_breakdown

# Function to generate cost-saving recommendations (same as previous code)
def generate_recommendations(complexity):
    recommendations = []

    if complexity <= 3:
        recommendations.append("Simplify your design to reduce material and labor costs.")
        recommendations.append("Consider using standard materials to lower material expenses.")
    elif 3 < complexity <= 7:
        recommendations.append("Optimize the design for efficient 3D printing.")
        recommendations.append("Explore different material options to balance cost and quality.")
    else:
        recommendations.append("Collaborate with experienced professionals to tackle complex projects.")
        recommendations.append("Invest in advanced materials and technologies for high-quality results.")

    return recommendations

# Function to generate and download the report as a PDF
def download_report_as_pdf(dimensions, material, complexity, estimated_cost, cost_breakdown, recommendations):
    # Create a PDF report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="3D Model Cost Estimator Report", ln=True, align="C")
    pdf.ln(10)

    # Project details
    pdf.cell(200, 10, txt="Project Details:", ln=True, align="L")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"- Dimensions: {dimensions[0]} cm x {dimensions[1]} cm", align="L")
    pdf.multi_cell(0, 10, f"- Material: {material}", align="L")
    pdf.multi_cell(0, 10, f"- Complexity: {complexity} (1 = Simple, 10 = Complex)", align="L")
    pdf.ln(10)

    # Estimated cost
    pdf.cell(200, 10, txt="Estimated Cost:", ln=True, align="L")
    pdf.multi_cell(0, 10, f"- The estimated cost for your project is $ {estimated_cost:.2f}", align="L")
    pdf.ln(10)

    # Cost breakdown
    pdf.cell(200, 10, txt="Cost Breakdown:", ln=True, align="L")
    pdf.multi_cell(0, 10, f"- Base Cost: $ {cost_breakdown['base_cost']:.2f}", align="L")
    pdf.multi_cell(0, 10, f"- Material Cost: $ {cost_breakdown['material_cost']:.2f}", align="L")
    pdf.multi_cell(0, 10, f"- Complexity Cost: $ {cost_breakdown['complexity_cost']:.2f}", align="L")
    pdf.ln(10)

    # Cost-saving tips
    pdf.cell(200, 10, txt="Cost-Saving Tips:", ln=True, align="L")
    if recommendations:
        for i, recommendation in enumerate(recommendations, 1):
            pdf.multi_cell(0, 10, f"{i}. {recommendation}", align="L")
    else:
        pdf.multi_cell(0, 10, "No specific recommendations for the selected complexity.", align="L")

    # Save the PDF to a file
    pdf_filename = "3d_model_cost_report.pdf"
    pdf.output(pdf_filename)

    # Provide a download link for the PDF
    with open(pdf_filename, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(
            label="Download Report as PDF",
            data=pdf_bytes,
            key="pdf_button",
            file_name=pdf_filename,
        )

# Run the app
if __name__ == "__main__":
    main()
