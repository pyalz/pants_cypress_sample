describe("Visits google", () => {
  it("searchbar exists", () => {
    cy.visit("https://google.com");
    cy.get("#APjFqb").type("Hello").type("{enter}");
  });
});
