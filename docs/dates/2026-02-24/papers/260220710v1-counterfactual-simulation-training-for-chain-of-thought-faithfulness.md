---
layout: default
title: Counterfactual Simulation Training for Chain-of-Thought Faithfulness
---

# Counterfactual Simulation Training for Chain-of-Thought Faithfulness
**arXiv**：[2602.20710v1](https://arxiv.org/abs/2602.20710) · [PDF](https://arxiv.org/pdf/2602.20710.pdf)  
**作者**：Peter Hase, Christopher Potts  

**一句话要点**：提出反事实模拟训练以提升思维链忠实度，应用于监控与通用推理场景。

**关键词**：思维链忠实度, 反事实模拟训练, 模型监控, 可解释性, 大语言模型, 推理泛化

## 3 点简述
- 核心问题：思维链忠实度不足限制模型推理可解释性，需改进监控与泛化能力。
- 方法要点：通过奖励反事实输入下模拟器准确预测模型输出的思维链，提升忠实度。
- 实验或效果：在235B参数模型中，监控准确率提升35点，模拟性提升2点，优于提示基线。

## 摘要（原文）

> Inspecting Chain-of-Thought reasoning is among the most common means of understanding why an LLM produced its output. But well-known problems with CoT faithfulness severely limit what insights can be gained from this practice. In this paper, we introduce a training method called Counterfactual Simulation Training (CST), which aims to improve CoT faithfulness by rewarding CoTs that enable a simulator to accurately predict a model's outputs over counterfactual inputs. We apply CST in two settings: (1) CoT monitoring with cue-based counterfactuals, to detect when models rely on spurious features, reward hack, or are sycophantic, and (2) counterfactual simulation over generic model-based counterfactuals, to encourage models to produce more faithful, generalizable reasoning in the CoT. Experiments with models up to 235B parameters show that CST can substantially improve monitor accuracy on cue-based counterfactuals (by 35 accuracy points) as well as simulatability over generic counterfactuals (by 2 points). We further show that: (1) CST outperforms prompting baselines, (2) rewriting unfaithful CoTs with an LLM is 5x more efficient than RL alone, (3) faithfulness improvements do not generalize to dissuading cues (as opposed to persuading cues), and (4) larger models do not show more faithful CoT out of the box, but they do benefit more from CST. These results suggest that CST can improve CoT faithfulness in general, with promising applications for CoT monitoring. Code for experiments in this paper is available at https://github.com/peterbhase/counterfactual-simulation-training

