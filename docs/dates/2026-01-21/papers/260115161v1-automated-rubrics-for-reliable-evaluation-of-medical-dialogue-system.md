---
layout: default
title: Automated Rubrics for Reliable Evaluation of Medical Dialogue Systems
---

# Automated Rubrics for Reliable Evaluation of Medical Dialogue Systems
**arXiv**：[2601.15161v1](https://arxiv.org/abs/2601.15161) · [PDF](https://arxiv.org/pdf/2601.15161.pdf)  
**作者**：Yinzhu Chen, Abdine Maiga, Hossein A. Rahmani, Emine Yilmaz  

**一句话要点**：提出检索增强多智能体框架以自动化生成医疗对话系统评估准则

**关键词**：医疗对话系统, 评估准则自动化, 检索增强生成, 多智能体框架, 临床意图对齐, 响应优化

## 3 点简述
- 核心问题：医疗LLMs存在幻觉和不安全建议，通用指标难以检测细微临床错误，专家评估准则成本高且难扩展。
- 方法要点：基于权威医学证据，通过分解检索内容为原子事实并结合用户交互约束，生成可验证的细粒度评估准则。
- 实验或效果：在HealthBench上，临床意图对齐分数达60.12%，显著优于GPT-4o基线，AUROC为0.977，并能指导响应优化提升9.2%。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly used for clinical decision support, where hallucinations and unsafe suggestions may pose direct risks to patient safety. These risks are particularly challenging as they often manifest as subtle clinical errors that evade detection by generic metrics, while expert-authored fine-grained rubrics remain costly to construct and difficult to scale. In this paper, we propose a retrieval-augmented multi-agent framework designed to automate the generation of instance-specific evaluation rubrics. Our approach grounds evaluation in authoritative medical evidence by decomposing retrieved content into atomic facts and synthesizing them with user interaction constraints to form verifiable, fine-grained evaluation criteria. Evaluated on HealthBench, our framework achieves a Clinical Intent Alignment (CIA) score of 60.12%, a statistically significant improvement over the GPT-4o baseline (55.16%). In discriminative tests, our rubrics yield a mean score delta ($μ_Δ = 8.658$) and an AUROC of 0.977, nearly doubling the quality separation achieved by GPT-4o baseline (4.972). Beyond evaluation, our rubrics effectively guide response refinement, improving quality by 9.2% (from 59.0% to 68.2%). This provides a scalable and transparent foundation for both evaluating and improving medical LLMs. The code is available at https://anonymous.4open.science/r/Automated-Rubric-Generation-AF3C/.

