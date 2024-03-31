"use client"

// Import necessary dependencies and styles
import { useSession } from "next-auth/react";
import PasswordChangeModal from "@/components/password_change";
import { DashboardLoader } from "@/components/skeleton_loader"
import { useRouter } from 'next/navigation';
import Link from "next/link";

// Define the Dashboard component
export default function Dashboard() {
  // Retrieve user session and status
  const { data: session, status } = useSession({ required: true });

  // Use Router
  const router = useRouter();

  // Loading state
  if (status === "loading") {
    return <DashboardLoader />; // Render dashboard skeleton loader while loading
  }

  // If there is no session, redirect to signin
  // else render dashboard
  if (!session && status === "unauthenticated") {
    router.push('/auth/signin')
    return null; // return null whilst routing
  } else {
    return (
      <div className="m-8 relative">
        {/* Dashboard Navigation Section */}
        <div className="sticky top-0 z-50 bg-white/10 rounded-lg p-4 flex items-center justify-between">
          <div className="flex items-center">
            <p className="capitalize text-lg text-white">Hello {session.user.username || 'boss'},</p>
          </div>
          <div className="flex items-center space-x-4">
            <Link href="/" className='px-4 py-2 bg-neutral-500 text-white rounded-lg hover:bg-amber-500'>Home</Link>
            <PasswordChangeModal />
            <button onClick={() => { window.location.href = "/auth/signout"; }} className="px-4 py-2 bg-neutral-500 text-white rounded-lg hover:bg-amber-500">
              Sign out
            </button>
          </div>
        </div>

        {/* Centered below the top left and top right */}
        <div className="mt-20">
          <p className="text-center text-white text-lg mb-4">Hey 👋, its <span className='animate-pulse text-amber-500 text-lg'>Quimer 🤗</span> your prep buddy.</p>
          <p className="capitalize text-center text-white text-lg mb-4">Member Since: {session.user.date_joined} </p>
          <p className="capitalize text-center text-white text-lg mb-4">Last Login: {session.user.last_login} </p>
        </div>
      </div>
    );
  }
}
