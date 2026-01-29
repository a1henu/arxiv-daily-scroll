---
layout: default
title: OS-Marathon: Benchmarking Computer-Use Agents on Long-Horizon Repetitive Tasks
---

# OS-Marathon: Benchmarking Computer-Use Agents on Long-Horizon Repetitive Tasks
**arXiv**：[2601.20650v1](https://arxiv.org/abs/2601.20650) · [PDF](https://arxiv.org/pdf/2601.20650.pdf)  
**作者**：Jing Wu, Daphne Barretto, Yiye Chen, Nicholas Gydé, Yanan Jian, Yuhang He, Vibhav Vineet  

**一句话要点**：提出OS-Marathon基准测试以评估计算机使用代理在长时程重复任务上的性能

**关键词**：计算机使用代理, 长时程任务, 基准测试, 重复工作流, 少量示例学习, 自动化评估

## 3 点简述
- 核心问题：缺乏评估计算机使用代理在长时程重复任务上的基准测试，阻碍了该领域发展。
- 方法要点：构建包含242个任务的基准，并引入基于少量示例的演示方法以高效教授代理工作流逻辑。
- 实验或效果：广泛实验展示了任务的挑战性和所提方法的有效性，支持代理在未见数据上执行类似工作流。

## 摘要（原文）

> Long-horizon, repetitive workflows are common in professional settings, such as processing expense reports from receipts and entering student grades from exam papers. These tasks are often tedious for humans since they can extend to extreme lengths proportional to the size of the data to process. However, they are ideal for Computer-Use Agents (CUAs) due to their structured, recurring sub-workflows with logic that can be systematically learned. Identifying the absence of an evaluation benchmark as a primary bottleneck, we establish OS-Marathon, comprising 242 long-horizon, repetitive tasks across 2 domains to evaluate state-of-the-art (SOTA) agents. We then introduce a cost-effective method to construct a condensed demonstration using only few-shot examples to teach agents the underlying workflow logic, enabling them to execute similar workflows effectively on larger, unseen data collections. Extensive experiments demonstrate both the inherent challenges of these tasks and the effectiveness of our proposed method. Project website: https://os-marathon.github.io/.

