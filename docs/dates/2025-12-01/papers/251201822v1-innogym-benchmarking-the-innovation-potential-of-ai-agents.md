---
layout: default
title: InnoGym: Benchmarking the Innovation Potential of AI Agents
---

# InnoGym: Benchmarking the Innovation Potential of AI Agents
**arXiv**：[2512.01822v1](https://arxiv.org/abs/2512.01822) · [PDF](https://arxiv.org/pdf/2512.01822.pdf)  
**作者**：Jintian Zhang, Kewei Xu, Jingsheng Zheng, Zhuoyun Yu, Yuqi Zhu, Yujie Luo, Lanning Wei, Shuofei Qiao, Lun Du, Da Zheng, Shumin Deng, Huajun Chen, Ningyu Zhang  

**一句话要点**：提出InnoGym基准与框架，以评估AI代理在真实工程与科学任务中的创新潜力。

**关键词**：AI代理评估, 创新基准, 性能增益, 方法新颖性, 工程科学任务, 统一执行环境

## 3 点简述
- 现有基准主要衡量正确性，忽视解决方案方法的多样性，创新需兼顾答案正确性与方法原创性。
- InnoGym引入性能增益和新颖性两个互补指标，并包含18个标准化任务及iGym统一执行环境。
- 实验显示AI代理能产生新颖方法，但鲁棒性不足限制性能增益，突显创造力与有效性间的差距。

## 摘要（原文）

> LLMs and Agents have achieved impressive progress in code generation, mathematical reasoning, and scientific discovery. However, existing benchmarks primarily measure correctness, overlooking the diversity of methods behind solutions. True innovation depends not only on producing correct answers but also on the originality of the approach. We present InnoGym, the first benchmark and framework designed to systematically evaluate the innovation potential of AI agents. InnoGym introduces two complementary metrics: performance gain, which measures improvement over the best-known solutions, and novelty, which captures methodological differences from prior approaches. The benchmark includes 18 carefully curated tasks from real-world engineering and scientific domains, each standardized through resource filtering, evaluator validation, and solution collection. In addition, we provide iGym, a unified execution environment for reproducible and long-horizon evaluations. Extensive experiments show that while some agents produce novel approaches, their lack of robustness limits performance gains. These results highlight a key gap between creativity and effectiveness, underscoring the need for benchmarks that evaluate both.

