---
layout: default
title: Rethinking Video Generation Model for the Embodied World
---

# Rethinking Video Generation Model for the Embodied World
**arXiv**：[2601.15282v1](https://arxiv.org/abs/2601.15282) · [PDF](https://arxiv.org/pdf/2601.15282.pdf)  
**作者**：Yufan Deng, Zilin Pan, Hongyu Zhang, Xiaojie Li, Ruoqing Hu, Yufei Ding, Yiming Zou, Yan Zeng, Daquan Zhou  

**一句话要点**：提出RBench基准与RoVid-X数据集，以评估和提升机器人视频生成的物理真实性。

**关键词**：机器人视频生成, 物理真实性评估, 基准测试, 数据集构建, 视频生成模型, 具身智能

## 3 点简述
- 核心问题：机器人视频生成缺乏标准化基准，难以评估物理真实性和任务正确性。
- 方法要点：引入RBench基准评估五个任务域和四种机器人形态，并构建RoVid-X数据集提供高质量训练数据。
- 实验或效果：评估25个模型显示物理行为生成不足，RBench与人类评估相关性达0.96，RoVid-X包含400万标注视频片段。

## 摘要（原文）

> Video generation models have significantly advanced embodied intelligence, unlocking new possibilities for generating diverse robot data that capture perception, reasoning, and action in the physical world. However, synthesizing high-quality videos that accurately reflect real-world robotic interactions remains challenging, and the lack of a standardized benchmark limits fair comparisons and progress. To address this gap, we introduce a comprehensive robotics benchmark, RBench, designed to evaluate robot-oriented video generation across five task domains and four distinct embodiments. It assesses both task-level correctness and visual fidelity through reproducible sub-metrics, including structural consistency, physical plausibility, and action completeness. Evaluation of 25 representative models highlights significant deficiencies in generating physically realistic robot behaviors. Furthermore, the benchmark achieves a Spearman correlation coefficient of 0.96 with human evaluations, validating its effectiveness. While RBench provides the necessary lens to identify these deficiencies, achieving physical realism requires moving beyond evaluation to address the critical shortage of high-quality training data. Driven by these insights, we introduce a refined four-stage data pipeline, resulting in RoVid-X, the largest open-source robotic dataset for video generation with 4 million annotated video clips, covering thousands of tasks and enriched with comprehensive physical property annotations. Collectively, this synergistic ecosystem of evaluation and data establishes a robust foundation for rigorous assessment and scalable training of video models, accelerating the evolution of embodied AI toward general intelligence.

