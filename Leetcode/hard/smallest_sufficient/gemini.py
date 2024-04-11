class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        # Create a dictionary to map skills to their indices in req_skills
        skill_to_index = {skill: i for i, skill in enumerate(req_skills)}

        # Initialize an empty team and a set to track missing skills
        team = []
        missing_skills = set(req_skills)

        for person_idx, person_skills in enumerate(people):
            # Convert person's skills to a set
            person_skills_set = set(person_skills)

            # Check if the person's skills cover any missing skills
            skills_covered = person_skills_set.intersection(missing_skills)
            if skills_covered:
            # Update missing skills and add person to the team
                missing_skills.difference_update(skills_covered)
                team.append(person_idx)

            # Early stopping if all missing skills are covered
            if not missing_skills:
                break

        return team