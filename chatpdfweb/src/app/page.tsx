import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { buttonVariants } from "@/components/ui/button";
import BackgroundGradient from "@/components/BackgroundGradient";
import ProductPreview from "@/components/ProductPreview";
import Image from "next/image";
import Steps from "@/components/Steps";
export default function Home() {
  return (
    <>
      <MaxWidthWrapper className="mb-6 mt-28 sm:mt-30 flex flex-col items-center justify-center text-center">
        <div className="mx-auto mb-4 flex max-w-fit items-center justify-center space-x-2 overflow-hidden rounded-full border border-gray-200 bg-white px-7 py-2 shadow-md backdrop-blur transition-all hover:border-gray-300 hover:bg-white/50">
          <p className="text-sm font-semibold text-gray-700">
            Chatpdf is now available in
            <span className="text-green-600"> beta!</span>
          </p>
        </div>
        <h1 className="max-w-4xl text-5xl font-bold md:text-6xl lg:text-7xl">
          Your Ultimate<span className="text-blue-600"> ChatPDF </span>
        </h1>
        <p className="mt-5 max-w-prose text-zinc-700 sm:text-lg">
          — ChatGPT Experience Powered by Your Own Documents
          <br />
          Instantly upload your documents and start a conversation!
        </p>

        <Link
          className={buttonVariants({
            size: "lg",
            className: "mt-5",
          })}
          href="/api/auth/login"
        >
          Get started <ArrowRight className="ml-2 h-5 w-5" />
        </Link>
        <Steps />
      </MaxWidthWrapper>
      {/* value proposition section */}
      {/* <BackgroundGradient>
        <ProductPreview />
      </BackgroundGradient> */}
    </>
  );
}
