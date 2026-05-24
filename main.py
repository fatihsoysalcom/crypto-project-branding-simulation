import random

class CryptoProject:
    def __init__(self, name, unique_features, brand_narrative):
        self.name = name
        self.unique_features = unique_features # List of strings representing distinct offerings
        self.brand_narrative = brand_narrative # String describing vision, mission, or story

    def calculate_brand_strength(self):
        """
        Simulates the 'brand strength' based on unique features and narrative.
        A higher score implies better branding and market differentiation,
        as discussed in the article about standing out post-token launch.
        """
        score = 0

        # Factor 1: Unique Value Proposition (from features)
        # Projects with more distinct features are better positioned to stand out.
        score += len(set(self.unique_features)) * 10
        if "decentralized governance" in self.unique_features:
            score += 5 # Specific valuable feature
        if "eco-friendly consensus" in self.unique_features:
            score += 7 # Another specific valuable feature

        # Factor 2: Brand Narrative Clarity and Appeal
        # A clear, compelling narrative helps transform a 'crypto asset' into a 'brand'.
        if self.brand_narrative:
            score += len(self.brand_narrative.split()) // 5 # Longer, more detailed narratives suggest more thought
            if "community-driven" in self.brand_narrative.lower():
                score += 10 # Keywords indicating strong brand identity
            if "long-term vision" in self.brand_narrative.lower():
                score += 8
            if "innovation" in self.brand_narrative.lower():
                score += 7
        else:
            score -= 20 # Penalize for lacking a narrative, making it harder to differentiate

        # Factor 3: Market Perception (simulated initial buzz/trust)
        # A small random component to simulate market unpredictability, 
        # but generally, stronger brands get a positive bias.
        score += random.randint(-5, 15)

        return max(0, score) # Ensure score is not negative

def main():
    print("--- Crypto Project Branding Simulation ---")

    # Example 1: A generic token with minimal branding
    generic_token = CryptoProject(
        name="BasicCoin",
        unique_features=["fast transactions"], # Common feature, not very unique
        brand_narrative="" # No clear narrative, struggles to define its unique value
    )
    print(f"\nProject: {generic_token.name}")
    print(f"  Features: {', '.join(generic_token.unique_features)}")
    print(f"  Narrative: '{generic_token.brand_narrative if generic_token.brand_narrative else 'None'}'")
    print(f"  Calculated Brand Strength: {generic_token.calculate_brand_strength()}")

    # Example 2: A token with some technical features but weak branding
    tech_token = CryptoProject(
        name="QuantumChain",
        unique_features=["quantum-resistant encryption", "cross-chain compatibility"], # Good tech
        brand_narrative="A new blockchain for secure data." # Simple, not very inspiring narrative
    )
    print(f"\nProject: {tech_token.name}")
    print(f"  Features: {', '.join(tech_token.unique_features)}")
    print(f"  Narrative: '{tech_token.brand_narrative}'")
    print(f"  Calculated Brand Strength: {tech_token.calculate_brand_strength()}")

    # Example 3: A project with strong unique features and a compelling brand narrative
    branded_project = CryptoProject(
        name="EcoVerse DAO",
        unique_features=["eco-friendly consensus", "decentralized governance", "NFT-based carbon credits"], # Distinct and valuable features
        brand_narrative="EcoVerse DAO is building a sustainable, community-driven future where blockchain technology empowers environmental initiatives and fosters a long-term vision for a greener planet through innovation and transparent governance." # Comprehensive, inspiring narrative
    )
    print(f"\nProject: {branded_project.name}")
    print(f"  Features: {', '.join(branded_project.unique_features)}")
    print(f"  Narrative: '{branded_project.brand_narrative}'")
    print(f"  Calculated Brand Strength: {branded_project.calculate_brand_strength()}")

    print("\n--- Summary ---")
    projects = [generic_token, tech_token, branded_project]
    for project in projects:
        print(f"'{project.name}': Brand Strength = {project.calculate_brand_strength()}")
    print("\nObservation: Projects with clear unique features and a strong brand narrative tend to have higher 'Brand Strength', reflecting better market differentiation and potential for long-term success, as highlighted in the article.")

if __name__ == "__main__":
    main()
