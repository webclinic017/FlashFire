import * as React from "react";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Link from "../Link";

export default function PlaceHolder() {
  return (
    <Container>
      <Typography variant="h4" component="h1" gutterBottom>
        MUI v5 + Next.js with TypeScript example
      </Typography>
      <Link href="/about" color="secondary">
        Go to the about page
      </Link>
    </Container>
  );
}