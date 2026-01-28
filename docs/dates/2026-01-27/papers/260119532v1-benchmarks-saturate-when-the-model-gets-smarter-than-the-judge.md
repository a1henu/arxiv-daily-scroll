---
layout: default
title: Benchmarks Saturate When The Model Gets Smarter Than The Judge
---

# Benchmarks Saturate When The Model Gets Smarter Than The Judge
**arXiv**：[2601.19532v1](https://arxiv.org/abs/2601.19532) · [PDF](https://arxiv.org/pdf/2601.19532.pdf)  
**作者**：Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis  

**一句话要点**：提出Omni-MATH-2数据集以解决大语言模型基准测试中数据集噪声和评估者误差问题

**关键词**：基准测试, 数据集噪声, 评估者误差, 大语言模型, 数学问题评估

## 3 点简述
- 核心问题：基准测试因数据集不准确和评估方法缺陷而失效，影响模型性能评估
- 方法要点：手动修订Omni-MATH数据集，创建清洁子集和标记子集，确保问题可编译、可解和可验证
- 实验或效果：比较GPT-5 mini与Omni-Judge，揭示评估者间显著差异，专家标注显示Omni-Judge在96.4%的争议中错误

## 摘要（原文）

> Benchmarks are important tools to track progress in the development of Large Language Models (LLMs), yet inaccuracies in datasets and evaluation methods consistently undermine their effectiveness. Here, we present Omni-MATH-2, a manually revised version of the Omni-MATH dataset comprising a clean, exact-answer subset ($n{=}4181$) and a tagged, non-standard subset ($n{=}247$). Each problem was audited to ensure LaTeX compilability, solvability and verifiability, which involved adding missing figures or information, labeling problems requiring a proof, estimation or image, and removing clutter. This process significantly reduces dataset-induced noise, thereby providing a more precise assessment of model performance. The annotated dataset also allows us to evaluate judge-induced noise by comparing GPT-5 mini with the original Omni-Judge, revealing substantial discrepancies between judges on both the clean and tagged problem subsets. Expert annotations reveal that Omni-Judge is wrong in $96.4\%$ of the judge disagreements, indicating its inability to differentiate between models' abilities, even well before saturation of the benchmark occurs. As problems become more challenging, we find that increasingly competent judges become essential in order to prevent judge errors from masking genuine differences between models. Finally, neither judge identifies the present failure modes for the subset of tagged problems, demonstrating that dataset quality and judge reliability are both critical to develop accurate benchmarks of model performance.

