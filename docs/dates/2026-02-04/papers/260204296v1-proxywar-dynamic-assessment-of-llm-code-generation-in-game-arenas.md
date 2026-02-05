---
layout: default
title: ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas
---

# ProxyWar: Dynamic Assessment of LLM Code Generation in Game Arenas
**arXiv**：[2602.04296v1](https://arxiv.org/abs/2602.04296) · [PDF](https://arxiv.org/pdf/2602.04296.pdf)  
**作者**：Wenjun Peng, Xinyu Wang, Qi Wu  

**一句话要点**：提出ProxyWar框架，通过游戏竞技环境动态评估LLM代码生成质量

**关键词**：代码生成评估, 动态测试, 游戏竞技, 多代理系统, LLM性能分析

## 3 点简述
- 核心问题：现有LLM代码生成评估依赖静态基准和简单指标，无法反映真实世界动态性能
- 方法要点：在多样化竞争游戏环境中嵌入LLM生成代理，结合自动测试、迭代修复和多代理锦标赛进行综合评估
- 实验或效果：应用于前沿代码生成模型和游戏，揭示基准分数与动态性能的显著差异，发现被忽视的局限和改进机会

## 摘要（原文）

> Large language models (LLMs) have revolutionized automated code generation, yet the evaluation of their real-world effectiveness remains limited by static benchmarks and simplistic metrics. We present ProxyWar, a novel framework that systematically assesses code generation quality by embedding LLM-generated agents within diverse, competitive game environments. Unlike existing approaches, ProxyWar evaluates not only functional correctness but also the operational characteristics of generated programs, combining automated testing, iterative code repair, and multi-agent tournaments to provide a holistic view of program behavior. Applied to a range of state-of-the-art coders and games, our approach uncovers notable discrepancies between benchmark scores and actual performance in dynamic settings, revealing overlooked limitations and opportunities for improvement. These findings highlight the need for richer, competition-based evaluation of code generation. Looking forward, ProxyWar lays a foundation for research into LLM-driven algorithm discovery, adaptive problem solving, and the study of practical efficiency and robustness, including the potential for models to outperform hand-crafted agents. The project is available at https://github.com/xinke-wang/ProxyWar.

