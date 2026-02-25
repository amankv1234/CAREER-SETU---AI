"use client";
import { motion } from "framer-motion";
import Link from "next/link";
import Navbar from "@/components/Navbar";
import {
    TrendingUp, Target, BookOpen, Briefcase, FileText, MessageSquare,
    ChevronRight, Sparkles, Zap, Star, ArrowUpRight, Clock, Award
} from "lucide-react";

const CAREER_SCORE = 72;
const RECOMMENDED_CAREERS = [
    { title: "Full Stack Developer", match: 85, salary: "₹8-20 LPA", growth: "+25%", demand: "High" },
    { title: "Data Scientist", match: 68, salary: "₹10-30 LPA", growth: "+35%", demand: "High" },
    { title: "Cloud Engineer", match: 62, salary: "₹12-25 LPA", growth: "+30%", demand: "High" },
];

const QUICK_ACTIONS = [
    { label: "Analyze Resume", href: "/resume", icon: FileText, color: "from-primary-500 to-primary-700" },
    { label: "Skill Gap Report", href: "/skills", icon: Target, color: "from-accent-purple to-pink-600" },
    { label: "Learning Roadmap", href: "/roadmap", icon: BookOpen, color: "from-accent-cyan to-blue-600" },
    { label: "Find Jobs", href: "/jobs", icon: Briefcase, color: "from-accent-emerald to-green-700" },
    { label: "Mock Interview", href: "/interview", icon: MessageSquare, color: "from-accent-amber to-orange-600" },
];

const SKILL_SUMMARY = [
    { name: "React", level: 80 },
    { name: "Python", level: 65 },
    { name: "SQL", level: 45 },
    { name: "Docker", level: 30 },
    { name: "Machine Learning", level: 20 },
];

const RECENT_ACTIVITY = [
    { action: "Resume analyzed", time: "2 hours ago", icon: FileText },
    { action: "Completed Python quiz", time: "1 day ago", icon: Award },
    { action: "Skill gap report generated", time: "2 days ago", icon: Target },
];

import { useState, useEffect } from "react";
import { api } from "@/lib/api";

function CircularProgress({ value, size = 120, stroke = 8 }: { value: number; size?: number; stroke?: number }) {
    const radius = (size - stroke) / 2;
    const circumference = radius * 2 * Math.PI;
    const offset = circumference - (value / 100) * circumference;

    return (
        <div className="relative inline-flex items-center justify-center">
            <svg width={size} height={size} className="-rotate-90">
                <circle cx={size / 2} cy={size / 2} r={radius} stroke="rgba(99,102,241,0.1)" strokeWidth={stroke} fill="none" />
                <motion.circle
                    cx={size / 2} cy={size / 2} r={radius}
                    stroke="url(#scoreGrad)" strokeWidth={stroke} fill="none"
                    strokeLinecap="round"
                    initial={{ strokeDashoffset: circumference }}
                    animate={{ strokeDashoffset: offset }}
                    transition={{ duration: 1.5, ease: "easeOut" }}
                    strokeDasharray={circumference}
                />
                <defs>
                    <linearGradient id="scoreGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                        <stop offset="0%" stopColor="#6366f1" />
                        <stop offset="100%" stopColor="#a855f7" />
                    </linearGradient>
                </defs>
            </svg>
            <div className="absolute text-center">
                <div className="text-3xl font-bold font-display text-white">{value}</div>
                <div className="text-xs text-dark-400">/ 100</div>
            </div>
        </div>
    );
}

export default function DashboardPage() {
    const [stats, setStats] = useState<{
        careerScore: number;
        recommendations: any[];
        skills: any[];
    }>({
        careerScore: 72,
        recommendations: [],
        skills: []
    });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadDashboard() {
            try {
                const profile = await api.getProfile();
                const recommendations = await api.getRecommendations(profile.skills);
                setStats({
                    careerScore: recommendations[0]?.match_score || 72,
                    recommendations: recommendations,
                    skills: profile.skills.map((s: string) => ({ name: s, level: 60 + Math.random() * 30 }))
                });
            } catch (error) {
                console.error("Failed to load dashboard:", error);
            } finally {
                setLoading(false);
            }
        }
        loadDashboard();
    }, []);

    const CAREER_SCORE = stats.careerScore;
    const RECOMMENDED_CAREERS = stats.recommendations.length > 0 ? stats.recommendations.map(r => ({
        title: r.title,
        match: Math.round(r.match_score),
        salary: r.salary,
        growth: r.growth,
        demand: r.demand
    })) : [
        { title: "Full Stack Developer", match: 85, salary: "₹8-20 LPA", growth: "+25%", demand: "High" },
        { title: "Data Scientist", match: 68, salary: "₹10-30 LPA", growth: "+35%", demand: "High" },
        { title: "Cloud Engineer", match: 62, salary: "₹12-25 LPA", growth: "+30%", demand: "High" },
    ];

    const SKILL_SUMMARY = stats.skills.length > 0 ? stats.skills : [
        { name: "React", level: 80 },
        { name: "Python", level: 65 },
        { name: "SQL", level: 45 },
        { name: "Docker", level: 30 },
        { name: "Machine Learning", level: 20 },
    ];

    const QUICK_ACTIONS = [
        { label: "Analyze Resume", href: "/resume", icon: FileText, color: "from-primary-500 to-primary-700" },
        { label: "Skill Gap Report", href: "/skills", icon: Target, color: "from-accent-purple to-pink-600" },
        { label: "Learning Roadmap", href: "/roadmap", icon: BookOpen, color: "from-accent-cyan to-blue-600" },
        { label: "Find Jobs", href: "/jobs", icon: Briefcase, color: "from-accent-emerald to-green-700" },
        { label: "Mock Interview", href: "/interview", icon: MessageSquare, color: "from-accent-amber to-orange-600" },
    ];

    const RECENT_ACTIVITY = [
        { action: "Resume analyzed", time: "2 hours ago", icon: FileText },
        { action: "Completed Python quiz", time: "1 day ago", icon: Award },
        { action: "Skill gap report generated", time: "2 days ago", icon: Target },
    ];

    return (
        <main className="min-h-screen bg-slate-950 text-white">
            <Navbar />

            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-12">
                <header className="mb-12">
                    <motion.h1
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        className="text-4xl font-bold font-display tracking-tight text-white sm:text-6xl mb-4"
                    >
                        Welcome back, <span className="text-secondary-400">Sachin</span>.
                    </motion.h1>
                    <p className="text-dark-400 text-lg max-w-2xl">
                        Your professional journey is 72% complete. Take the next step to boost your career score.
                    </p>
                </header>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    {/* Left Column: Stats & Recommendations */}
                    <div className="lg:col-span-2 space-y-8">
                        <section className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <motion.div
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                className="glass-card p-6 flex flex-col items-center justify-center text-center group"
                            >
                                <CircularProgress value={CAREER_SCORE} />
                                <h3 className="mt-4 text-xl font-bold text-white">Career Score</h3>
                                <p className="text-dark-400 text-sm mt-1">Based on your current skill profile & market demand</p>
                                <div className="mt-4 flex items-center gap-1 text-accent-emerald text-sm font-medium">
                                    <TrendingUp className="w-4 h-4" /> +12% this month
                                </div>
                            </motion.div>

                            <motion.div
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: 0.1 }}
                                className="glass-card p-6 flex flex-col justify-between"
                            >
                                <div>
                                    <h3 className="text-xl font-bold text-white flex items-center gap-2 mb-4">
                                        <Sparkles className="w-5 h-5 text-accent-cyan" />
                                        Next Goal
                                    </h3>
                                    <p className="text-dark-300">Complete the **System Architecture** module to reach <span className="text-accent-cyan font-bold font-display text-lg">80+</span> score.</p>
                                </div>
                                <button className="btn-secondary w-full mt-6 group">
                                    Resume Learning
                                    <ChevronRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                                </button>
                            </motion.div>
                        </section>

                        <section>
                            <div className="flex items-center justify-between mb-6">
                                <h2 className="text-2xl font-bold text-white flex items-center gap-2">
                                    <Target className="w-6 h-6 text-primary-400" />
                                    Top Career Matches
                                </h2>
                                <Link href="/jobs" className="text-sm text-primary-400 hover:text-primary-300 flex items-center gap-1">
                                    View Job Explorer <ArrowUpRight className="w-3 h-3" />
                                </Link>
                            </div>
                            <div className="space-y-4">
                                {RECOMMENDED_CAREERS.map((career, i) => (
                                    <motion.div
                                        key={career.title}
                                        initial={{ opacity: 0, x: -20 }}
                                        animate={{ opacity: 1, x: 0 }}
                                        transition={{ delay: i * 0.1 + 0.2 }}
                                        className="glass-card p-4 hover:bg-white/[0.05] transition-colors cursor-pointer group"
                                    >
                                        <div className="flex items-center justify-between">
                                            <div className="flex items-center gap-4">
                                                <div className="w-12 h-12 rounded-xl bg-primary-500/10 border border-primary-500/20 flex items-center justify-center text-primary-400 font-bold font-display text-lg">
                                                    {career.match}%
                                                </div>
                                                <div>
                                                    <h4 className="text-white font-semibold group-hover:text-primary-300 transition-colors">{career.title}</h4>
                                                    <div className="flex items-center gap-3 mt-1 text-xs text-dark-400">
                                                        <span className="flex items-center gap-1"><Briefcase className="w-3 h-3" /> {career.demand} Demand</span>
                                                        <span className="flex items-center gap-1"><TrendingUp className="w-3 h-3" /> {career.growth} Growth</span>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="text-right">
                                                <div className="text-sm font-bold text-accent-emerald">{career.salary}</div>
                                                <div className="text-xs text-dark-500 mt-1">Avg. CTC</div>
                                            </div>
                                        </div>
                                    </motion.div>
                                ))}
                            </div>
                        </section>
                    </div>

                    {/* Right Column: Actions & Activity */}
                    <div className="space-y-8">
                        <section className="glass-card p-6">
                            <h3 className="text-lg font-bold text-white mb-6 flex items-center gap-2">
                                <Zap className="w-5 h-5 text-accent-amber" />
                                Quick Actions
                            </h3>
                            <div className="space-y-3">
                                {QUICK_ACTIONS.map((action) => (
                                    <Link
                                        key={action.label}
                                        href={action.href}
                                        className="flex items-center gap-4 p-3 rounded-xl hover:bg-white/[0.05] transition-colors group"
                                    >
                                        <div className={`w-10 h-10 rounded-lg bg-gradient-to-br ${action.color} p-2 flex items-center justify-center shadow-lg shadow-white/5`}>
                                            <action.icon className="w-5 h-5 text-white" />
                                        </div>
                                        <span className="text-sm font-medium text-dark-200 group-hover:text-white transition-colors">{action.label}</span>
                                        <ChevronRight className="w-4 h-4 ml-auto text-dark-600 group-hover:text-dark-400 group-hover:translate-x-1 transition-all" />
                                    </Link>
                                ))}
                            </div>
                        </section>

                        <section className="glass-card p-6">
                            <h3 className="text-lg font-bold text-white mb-6 flex items-center gap-2">
                                <Clock className="w-5 h-5 text-accent-purple" />
                                Recent Activity
                            </h3>
                            <div className="space-y-6">
                                {RECENT_ACTIVITY.map((act, i) => (
                                    <div key={i} className="flex gap-4 relative">
                                        {i !== RECENT_ACTIVITY.length - 1 && (
                                            <div className="absolute left-[19px] top-10 bottom-[-15px] w-0.5 bg-white/5" />
                                        )}
                                        <div className="w-10 h-10 rounded-full bg-slate-900 border border-white/5 flex items-center justify-center relative z-10">
                                            <act.icon className="w-4 h-4 text-dark-400" />
                                        </div>
                                        <div>
                                            <p className="text-sm text-dark-200 font-medium">{act.action}</p>
                                            <p className="text-xs text-dark-500 mt-1">{act.time}</p>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </section>
                    </div>
                </div>
            </div>
        </main>
    );
}
