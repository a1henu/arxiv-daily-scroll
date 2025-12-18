---
layout: default
title: FrontierCS: Evolving Challenges for Evolving Intelligence
---

# FrontierCS: Evolving Challenges for Evolving Intelligence
**arXiv**：[2512.15699v1](https://arxiv.org/abs/2512.15699) · [PDF](https://arxiv.org/pdf/2512.15699.pdf)  
**作者**：Qiuyang Mang, Wenhao Chai, Zhifei Li, Huanzhi Mao, Shang Zhou, Alexander Du, Hanchen Li, Shu Liu, Edwin Chen, Yichuan Wang, Xieting Chu, Zerui Cheng, Yuan Xu, Tian Xia, Zirui Wang, Tianneng Shi, Jianzhu Yao, Yilong Zhao, Qizheng Zhang, Charlie Ruan, Zeyu Shen, Kaiyuan Liu, Runyuan He, Dong Xing, Zerui Li, Zirong Zeng, Yige Jiang, Lufeng Cheng, Ziyi Zhao, Youran Sun, Wesley Zheng, Meiyuwang Zhang, Ruyi Ji, Xuechang Tu, Zihan Zheng, Zexing Chen, Kangyang Zhou, Zhaozi Wang, Jingbang Chen, Aleksandra Korolova, Peter Henderson, Pramod Viswanath, Vijay Ganesh, Saining Xie, Zhuang Liu, Dawn Song, Sewon Min, Ion Stoica, Joseph E. Gonzalez, Jingbo Shang, Alvin Cheung  

**一句话要点**：提出FrontierCS基准，针对未知最优解的开放性问题，评估计算机科学前沿推理能力。

**关键词**：开放性问题基准, 计算机科学前沿, 算法评估, 自动评估器, 推理模型, 专家解决方案

## 3 点简述
- 核心问题：现有基准多关注已知最优解任务，缺乏对未知最优解但可客观评估质量的开放性问题评估。
- 方法要点：设计156个开放性问题，涵盖算法与研究领域，提供专家参考解和自动评估器，支持可执行程序实现。
- 实验或效果：前沿推理模型在算法与研究任务上远落后于人类专家，增加推理预算无法弥补差距，模型易生成可行代码而非高质量算法。

## 摘要（原文）

> We introduce FrontierCS, a benchmark of 156 open-ended problems across diverse areas of computer science, designed and reviewed by experts, including CS PhDs and top-tier competitive programming participants and problem setters. Unlike existing benchmarks that focus on tasks with known optimal solutions, FrontierCS targets problems where the optimal solution is unknown, but the quality of a solution can be objectively evaluated. Models solve these tasks by implementing executable programs rather than outputting a direct answer. FrontierCS includes algorithmic problems, which are often NP-hard variants of competitive programming problems with objective partial scoring, and research problems with the same property. For each problem we provide an expert reference solution and an automatic evaluator. Combining open-ended design, measurable progress, and expert curation, FrontierCS provides a benchmark at the frontier of computer-science difficulty. Empirically, we find that frontier reasoning models still lag far behind human experts on both the algorithmic and research tracks, that increasing reasoning budgets alone does not close this gap, and that models often over-optimize for generating merely workable code instead of discovering high-quality algorithms and system designs.

