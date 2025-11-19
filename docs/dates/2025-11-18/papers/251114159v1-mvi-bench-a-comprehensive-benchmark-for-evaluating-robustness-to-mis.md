---
layout: default
title: MVI-Bench: A Comprehensive Benchmark for Evaluating Robustness to Misleading Visual Inputs in LVLMs
---

# MVI-Bench: A Comprehensive Benchmark for Evaluating Robustness to Misleading Visual Inputs in LVLMs
**arXiv**：[2511.14159v1](https://arxiv.org/abs/2511.14159) · [PDF](https://arxiv.org/pdf/2511.14159.pdf)  
**作者**：Huiyi Chen, Jiawei Peng, Dehai Min, Changchang Sun, Kaijie Chen, Yan Yan, Xu Yang, Lu Cheng  

**一句话要点**：提出MVI-Bench基准以评估LVLM对误导性视觉输入的鲁棒性

**关键词**：大型视觉语言模型, 鲁棒性评估, 误导性视觉输入, 视觉问答基准, MVI-Sensitivity指标, 视觉原语分类

## 3 点简述
- 现有基准多关注文本误导，忽略视觉误导对LVLM鲁棒性的影响
- 基于视觉原语构建三层误导输入分类，并收集1248个VQA实例
- 引入MVI-Sensitivity指标，评估18个LVLM显示显著脆弱性

## 摘要（原文）

> Evaluating the robustness of Large Vision-Language Models (LVLMs) is essential for their continued development and responsible deployment in real-world applications. However, existing robustness benchmarks typically focus on hallucination or misleading textual inputs, while largely overlooking the equally critical challenge posed by misleading visual inputs in assessing visual understanding. To fill this important gap, we introduce MVI-Bench, the first comprehensive benchmark specially designed for evaluating how Misleading Visual Inputs undermine the robustness of LVLMs. Grounded in fundamental visual primitives, the design of MVI-Bench centers on three hierarchical levels of misleading visual inputs: Visual Concept, Visual Attribute, and Visual Relationship. Using this taxonomy, we curate six representative categories and compile 1,248 expertly annotated VQA instances. To facilitate fine-grained robustness evaluation, we further introduce MVI-Sensitivity, a novel metric that characterizes LVLM robustness at a granular level. Empirical results across 18 state-of-the-art LVLMs uncover pronounced vulnerabilities to misleading visual inputs, and our in-depth analyses on MVI-Bench provide actionable insights that can guide the development of more reliable and robust LVLMs. The benchmark and codebase can be accessed at https://github.com/chenyil6/MVI-Bench.

