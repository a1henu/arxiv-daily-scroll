---
layout: default
title: Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification
---

# Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification
**arXiv**：[2601.15808v1](https://arxiv.org/abs/2601.15808) · [PDF](https://arxiv.org/pdf/2601.15808.pdf)  
**作者**：Yuxuan Wan, Tianqing Fang, Zaitang Li, Yintong Huo, Wenxuan Wang, Haitao Mi, Dong Yu, Michael R. Lyu  

**一句话要点**：提出基于验证的推理时缩放方法，通过测试时准则引导验证实现深度研究代理的自进化

**关键词**：深度研究代理, 推理时缩放, 准则引导验证, 自进化, 测试时精炼, 开源数据集

## 3 点简述
- 核心问题：现有深度研究代理依赖训练后增强，缺乏推理时自我改进能力。
- 方法要点：基于自动构建的失败分类法设计准则，开发DeepVerifier验证器进行迭代反馈与精炼。
- 实验或效果：在GAIA和XBench-DeepResearch挑战子集上实现8%-11%准确率提升，并发布开源数据集DeepVerifier-4K。

## 摘要（原文）

> Recent advances in Deep Research Agents (DRAs) are transforming automated knowledge discovery and problem-solving. While the majority of existing efforts focus on enhancing policy capabilities via post-training, we propose an alternative paradigm: self-evolving the agent's ability by iteratively verifying the policy model's outputs, guided by meticulously crafted rubrics. This approach gives rise to the inference-time scaling of verification, wherein an agent self-improves by evaluating its generated answers to produce iterative feedback and refinements. We derive the rubrics based on an automatically constructed DRA Failure Taxonomy, which systematically classifies agent failures into five major categories and thirteen sub-categories. We present DeepVerifier, a rubrics-based outcome reward verifier that leverages the asymmetry of verification and outperforms vanilla agent-as-judge and LLM judge baselines by 12%-48% in meta-evaluation F1 score. To enable practical self-evolution, DeepVerifier integrates as a plug-and-play module during test-time inference. The verifier produces detailed rubric-based feedback, which is fed back to the agent for iterative bootstrapping, refining responses without additional training. This test-time scaling delivers 8%-11% accuracy gains on challenging subsets of GAIA and XBench-DeepResearch when powered by capable closed-source LLMs. Finally, to support open-source advancement, we release DeepVerifier-4K, a curated supervised fine-tuning dataset of 4,646 high-quality agent steps focused on DRA verification. These examples emphasize reflection and self-critique, enabling open models to develop robust verification capabilities.

