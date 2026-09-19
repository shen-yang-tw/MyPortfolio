'use client';

import { motion } from 'framer-motion';
import { Card, CardContent } from '@/components/ui/card';
import { Code2, Database, Layers, Zap, Globe, GitBranch, Cloud, Terminal } from 'lucide-react';

const skillCategories = [
  {
    title: '前端框架',
    icon: Code2,
    skills: ['React 19', 'Next.js 16', 'Vue 3', 'TypeScript', 'JavaScript ES2024'],
  },
  {
    title: '樣式與設計',
    icon: Layers,
    skills: ['Tailwind CSS v4', 'CSS Modules', 'Framer Motion', 'shadcn/ui', 'Responsive Design'],
  },
  {
    title: '後端與資料庫',
    icon: Database,
    skills: ['Supabase', 'PostgreSQL', 'Server Actions', 'REST API', 'GraphQL'],
  },
  {
    title: '效能與架構',
    icon: Zap,
    skills: ['RSC', 'ISR', 'Code Splitting', 'Bundle Optimization', 'Core Web Vitals'],
  },
  {
    title: 'DevOps 與部署',
    icon: Cloud,
    skills: ['Vercel', 'Netlify', 'Docker', 'CI/CD', 'GitHub Actions'],
  },
  {
    title: '工具與實踐',
    icon: GitBranch,
    skills: ['Git / GitHub', 'Zod Validation', 'React Hook Form', 'Vitest', 'Playwright'],
  },
];

export function SkillsSection() {
  return (
    <section className="relative border-t border-border bg-card/30">
      <div className="absolute inset-0 bg-dot-pattern opacity-[0.02]" />
      <div className="relative mx-auto max-w-7xl px-4 py-20 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-100px' }}
          transition={{ duration: 0.5 }}
          className="mb-12 text-center"
        >
          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">
            技術<span className="text-gradient-primary">棧</span>
          </h2>
          <p className="mt-3 text-muted-foreground">
            橫跨前端、後端到部署的完整技術能力
          </p>
        </motion.div>

        <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {skillCategories.map((category, i) => (
            <motion.div
              key={category.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, margin: '-50px' }}
              transition={{ duration: 0.5, delay: i * 0.08 }}
            >
              <Card className="group h-full border-border bg-card/50 transition-all hover:border-primary/30 hover:shadow-lg">
                <CardContent className="p-6">
                  <div className="mb-4 flex items-center gap-3">
                    <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10 text-primary transition-all group-hover:scale-110 group-hover:bg-primary/20">
                      <category.icon className="h-5 w-5" />
                    </div>
                    <h3 className="font-semibold">{category.title}</h3>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {category.skills.map((skill) => (
                      <span
                        key={skill}
                        className="rounded-md border border-border bg-muted/50 px-2.5 py-1 text-xs font-medium text-muted-foreground transition-colors hover:border-primary/30 hover:text-foreground"
                      >
                        {skill}
                      </span>
                    ))}
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
