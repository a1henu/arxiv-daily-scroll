---
layout: default
title: The Erasure Illusion: Stress-Testing the Generalization of LLM Forgetting Evaluation
---

# The Erasure Illusion: Stress-Testing the Generalization of LLM Forgetting Evaluation
**arXiv**：[2512.19025v1](https://arxiv.org/abs/2512.19025) · [PDF](https://arxiv.org/pdf/2512.19025.pdf)  
**作者**：Hengrui Jia, Taoran Li, Jonas Guan, Varun Chandrasekaran  

**一句话要点**：提出自动化压力测试框架以评估大语言模型遗忘评估的泛化可靠性

**关键词**：大语言模型遗忘, 评估指标压力测试, 语义泛化检测, 自动化框架, 知识保留评估

## 3 点简述
- 核心问题：现有遗忘评估指标可能高估大语言模型遗忘成功，无法检测语义相邻知识的保留。
- 方法要点：构建语义衍生但嵌入空间不同的替代数据集，通过对比指标分数压力测试评估可靠性。
- 实验或效果：在三个大语言模型家族、三个数据集和七个标准指标上发现广泛不一致，揭示指标常高估遗忘成功。

## 摘要（原文）

> Machine unlearning aims to remove specific data influences from trained models, a capability essential for adhering to copyright laws and ensuring AI safety. Current unlearning metrics typically measure success by monitoring the model's performance degradation on the specific unlearning dataset ($D_u$). We argue that for Large Language Models (LLMs), this evaluation paradigm is insufficient and potentially misleading. Many real-world uses of unlearning--motivated by copyright or safety--implicitly target not only verbatim content in $D_u$, but also behaviors influenced by the broader generalizations the model derived from it. We demonstrate that LLMs can pass standard unlearning evaluation and appear to have ``forgotten'' the target knowledge, while simultaneously retaining strong capabilities on content that is semantically adjacent to $D_u$. This phenomenon indicates that erasing exact sentences does not necessarily equate to removing the underlying knowledge. To address this gap, we propose \name, an automated stress-testing framework that generates a surrogate dataset, $\tilde{D}_u$. This surrogate set is constructed to be semantically derived from $D_u$ yet sufficiently distinct in embedding space. By comparing unlearning metric scores between $D_u$ and $\tilde{D}_u$, we can stress-test the reliability of the metric itself. Our extensive evaluation across three LLM families (Llama-3-8B, Qwen2.5-7B, and Zephyr-7B-$β$), three distinct datasets, and seven standard metrics reveals widespread inconsistencies. We find that current metrics frequently overestimate unlearning success, failing to detect retained knowledge exposed by our stress-test datasets.

