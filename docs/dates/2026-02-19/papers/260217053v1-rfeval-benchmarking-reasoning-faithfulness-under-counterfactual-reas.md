---
layout: default
title: RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models
---

# RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models
**arXiv**：[2602.17053v1](https://arxiv.org/abs/2602.17053) · [PDF](https://arxiv.org/pdf/2602.17053.pdf)  
**作者**：Yunseok Han, Yejoon Lee, Jaeyoung Do  

**一句话要点**：提出RFEval基准以评估大型推理模型在反事实干预下的推理忠实性

**关键词**：推理忠实性, 反事实干预, 大型推理模型, 基准评估, 因果影响, 立场一致性

## 3 点简述
- 核心问题：大型推理模型常生成看似合理但未反映真实决策过程的推理，损害可靠性。
- 方法要点：定义推理忠实性为立场一致性和因果影响，通过输出级反事实干预进行测试。
- 实验或效果：评估12个开源模型，发现49.7%输出不忠实，准确性与忠实性关联弱。

## 摘要（原文）

> Large Reasoning Models (LRMs) exhibit strong performance, yet often produce rationales that sound plausible but fail to reflect their true decision process, undermining reliability and trust. We introduce a formal framework for reasoning faithfulness, defined by two testable conditions: stance consistency (a coherent stance linking reasoning to answer) and causal influence (the stated reasoning causally drives the answer under output-level interventions), explicitly decoupled from accuracy. To operationalize this, we present RFEval, a benchmark of 7,186 instances across seven tasks that probes faithfulness via controlled, output-level counterfactual interventions. Evaluating twelve open-source LRMs, we find unfaithfulness in 49.7% of outputs, predominantly from stance inconsistency. Failures are concentrated in brittle, convergent domains such as math and code, and correlate more with post-training regimes than with scale: within-family ablations indicate that adding current RL-style objectives on top of supervised fine-tuning can reduce reasoning faithfulness, even when accuracy is maintained. Crucially, accuracy is neither a sufficient nor a reliable proxy for faithfulness: once controlling for model and task, the accuracy-faithfulness link is weak and statistically insignificant. Our work establishes a rigorous methodology for auditing LRM reliability and shows that trustworthy AI requires optimizing not only for correct outcomes but also for the structural integrity of the reasoning process. Our code and dataset can be found at project page: $\href{https://aidaslab.github.io/RFEval/}{https://aidaslab.github.io/RFEval/}$

