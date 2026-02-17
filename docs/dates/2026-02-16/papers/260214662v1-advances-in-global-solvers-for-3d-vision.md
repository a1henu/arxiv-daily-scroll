---
layout: default
title: Advances in Global Solvers for 3D Vision
---

# Advances in Global Solvers for 3D Vision
**arXiv**：[2602.14662v1](https://arxiv.org/abs/2602.14662) · [PDF](https://arxiv.org/pdf/2602.14662.pdf)  
**作者**：Zhenjun Zhao, Heng Yang, Bangyan Liao, Yingping Zeng, Shaocheng Yan, Yingdong Gu, Peidong Liu, Yi Zhou, Haoang Li, Javier Civera  

**一句话要点**：综述全局求解器在三维视觉中的应用，系统分类三大范式并分析任务权衡。

**关键词**：全局求解器, 三维视觉, 非凸优化, 分支定界, 凸松弛, 渐进非凸性

## 3 点简述
- 核心问题：三维视觉中的非凸几何优化问题，传统方法依赖局部或启发式求解，缺乏可证明的全局最优解。
- 方法要点：提出基于分支定界、凸松弛和渐进非凸性的三大全局求解器范式，统一理论、算法和实际增强。
- 实验或效果：分析十个核心视觉任务，揭示最优性-鲁棒性-可扩展性权衡，为实际应用提供选择指南。

## 摘要（原文）

> Global solvers have emerged as a powerful paradigm for 3D vision, offering certifiable solutions to nonconvex geometric optimization problems traditionally addressed by local or heuristic methods. This survey presents the first systematic review of global solvers in geometric vision, unifying the field through a comprehensive taxonomy of three core paradigms: Branch-and-Bound (BnB), Convex Relaxation (CR), and Graduated Non-Convexity (GNC). We present their theoretical foundations, algorithmic designs, and practical enhancements for robustness and scalability, examining how each addresses the fundamental nonconvexity of geometric estimation problems. Our analysis spans ten core vision tasks, from Wahba problem to bundle adjustment, revealing the optimality-robustness-scalability trade-offs that govern solver selection. We identify critical future directions: scaling algorithms while maintaining guarantees, integrating data-driven priors with certifiable optimization, establishing standardized benchmarks, and addressing societal implications for safety-critical deployment. By consolidating theoretical foundations, practical advances, and broader impacts, this survey provides a unified perspective and roadmap toward certifiable, trustworthy perception for real-world applications. A continuously-updated literature summary and companion code tutorials are available at https://github.com/ericzzj1989/Awesome-Global-Solvers-for-3D-Vision.

