---
layout: default
title: Trustworthy Evaluation of Robotic Manipulation: A New Benchmark and AutoEval Methods
---

# Trustworthy Evaluation of Robotic Manipulation: A New Benchmark and AutoEval Methods
**arXiv**：[2601.18723v1](https://arxiv.org/abs/2601.18723) · [PDF](https://arxiv.org/pdf/2601.18723.pdf)  
**作者**：Mengyuan Liu, Juyi Sheng, Peiming Li, Ziyi Wang, Tianming Xu, Tiantian Xu, Hong Liu  

**一句话要点**：提出Eval-Actions基准与AutoEval架构，以解决机器人操作可信评估中的源真实性与执行质量问题。

**关键词**：机器人操作评估, 可信评估基准, 源真实性分析, 执行质量优化, 时空聚合, 运动平滑度校准

## 3 点简述
- 核心问题：现有评估方法依赖二元成功率，缺乏对源真实性和执行质量的信任维度分析。
- 方法要点：构建Eval-Actions基准，集成策略轨迹与人类遥操作数据，并设计AutoEval架构进行语义评估和运动平滑度优化。
- 实验或效果：AutoEval在EG和RG协议下SRCC达0.81和0.84，源区分准确率99.6%，提升评估可信度。

## 摘要（原文）

> Driven by the rapid evolution of Vision-Action and Vision-Language-Action models, imitation learning has significantly advanced robotic manipulation capabilities. However, evaluation methodologies have lagged behind, hindering the establishment of Trustworthy Evaluation for these behaviors. Current paradigms rely on binary success rates, failing to address the critical dimensions of trust: Source Authenticity (i.e., distinguishing genuine policy behaviors from human teleoperation) and Execution Quality (e.g., smoothness and safety). To bridge these gaps, we propose a solution that combines the Eval-Actions benchmark and the AutoEval architecture. First, we construct the Eval-Actions benchmark to support trustworthiness analysis. Distinct from existing datasets restricted to successful human demonstrations, Eval-Actions integrates VA and VLA policy execution trajectories alongside human teleoperation data, explicitly including failure scenarios. This dataset is structured around three core supervision signals: Expert Grading (EG), Rank-Guided preferences (RG), and Chain-of-Thought (CoT). Building on this, we propose the AutoEval architecture: AutoEval leverages Spatio-Temporal Aggregation for semantic assessment, augmented by an auxiliary Kinematic Calibration Signal to refine motion smoothness; AutoEval Plus (AutoEval-P) incorporates the Group Relative Policy Optimization (GRPO) paradigm to enhance logical reasoning capabilities. Experiments show AutoEval achieves Spearman's Rank Correlation Coefficients (SRCC) of 0.81 and 0.84 under the EG and RG protocols, respectively. Crucially, the framework possesses robust source discrimination capabilities, distinguishing between policy-generated and teleoperated videos with 99.6% accuracy, thereby establishing a rigorous standard for trustworthy robotic evaluation. Our project and code are available at https://term-bench.github.io/.

