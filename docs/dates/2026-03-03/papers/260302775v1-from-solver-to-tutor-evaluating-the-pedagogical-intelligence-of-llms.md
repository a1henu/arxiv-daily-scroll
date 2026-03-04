---
layout: default
title: From Solver to Tutor: Evaluating the Pedagogical Intelligence of LLMs with KMP-Bench
---

# From Solver to Tutor: Evaluating the Pedagogical Intelligence of LLMs with KMP-Bench
**arXiv**：[2603.02775v1](https://arxiv.org/abs/2603.02775) · [PDF](https://arxiv.org/pdf/2603.02775.pdf)  
**作者**：Weikang Shi, Houxing Ren, Junting Pan, Aojun Zhou, Ke Wang, Zimu Lu, Yunqiao Yang, Yuxuan Hu, Linda Wei, Mingjie Zhan, Hongsheng Li  

**一句话要点**：提出KMP-Bench基准以评估LLMs在K-8数学教学中的综合教学能力

**关键词**：数学教学评估, 多轮对话基准, 教学原则分析, 错误检测与纠正, 问题生成, 数据集构建

## 3 点简述
- 当前LLMs数学教学评估依赖简单指标，缺乏多轮教学效果评估
- KMP-Bench包含KMP-Dialogue和KMP-Skills模块，评估教学原则和基础能力
- 实验显示LLMs在可验证任务中表现好，但教学原则应用不足，微调后提升显著

## 摘要（原文）

> Large Language Models (LLMs) show significant potential in AI mathematical tutoring, yet current evaluations often rely on simplistic metrics or narrow pedagogical scenarios, failing to assess comprehensive, multi-turn teaching effectiveness. In this paper, we introduce KMP-Bench, a comprehensive K-8 Mathematical Pedagogical Benchmark designed to assess LLMs from two complementary perspectives. The first module, KMP-Dialogue, evaluates holistic pedagogical capabilities against six core principles (e.g., Challenge, Explanation, Feedback), leveraging a novel multi-turn dialogue dataset constructed by weaving together diverse pedagogical components. The second module, KMP-Skills, provides a granular assessment of foundational tutoring abilities, including multi-turn problem-solving, error detection and correction, and problem generation. Our evaluations on KMP-Bench reveal a key disparity: while leading LLMs excel at tasks with verifiable solutions, they struggle with the nuanced application of pedagogical principles. Additionally, we present KMP-Pile, a large-scale (150K) dialogue dataset. Models fine-tuned on KMP-Pile show substantial improvement on KMP-Bench, underscoring the value of pedagogically-rich training data for developing more effective AI math tutors.

