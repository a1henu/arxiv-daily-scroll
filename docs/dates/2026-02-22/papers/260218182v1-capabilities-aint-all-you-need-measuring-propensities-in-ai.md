---
layout: default
title: Capabilities Ain't All You Need: Measuring Propensities in AI
---

# Capabilities Ain't All You Need: Measuring Propensities in AI
**arXiv**：[2602.18182v1](https://arxiv.org/abs/2602.18182) · [PDF](https://arxiv.org/pdf/2602.18182.pdf)  
**作者**：Daniel Romero-Alvarado, Fernando Martínez-Plumed, Lorenzo Pacchiardi, Hugo Save, Siddhesh Milind Pawar, Behzad Mehrbakhsh, Pablo Antonio Moreno Casares, Ben Slater, Paolo Bova, Peter Romero, Zachary R. Tyler, Jonathan Prunty, Luning Sun, Jose Hernandez-Orallo  

**一句话要点**：提出双逻辑框架以测量AI倾向性，超越能力评估预测行为

**关键词**：AI倾向性测量, 双逻辑框架, 任务无关准则, LLM评估, 行为预测, 能力与倾向性结合

## 3 点简述
- AI评估聚焦能力，但倾向性影响性能与安全，传统IRT方法不适用
- 引入双逻辑公式定义理想带，结合任务无关准则估计倾向性
- 在LLM实验中验证倾向性测量可预测未知任务，结合能力提升预测力

## 摘要（原文）

> AI evaluation has primarily focused on measuring capabilities, with formal approaches inspired from Item Response Theory (IRT) being increasingly applied. Yet propensities - the tendencies of models to exhibit particular behaviours - play a central role in determining both performance and safety outcomes. However, traditional IRT describes a model's success on a task as a monotonic function of model capabilities and task demands, an approach unsuited to propensities, where both excess and deficiency can be problematic. Here, we introduce the first formal framework for measuring AI propensities by using a bilogistic formulation for model success, which attributes high success probability when the model's propensity is within an "ideal band". Further, we estimate the limits of the ideal band using LLMs equipped with newly developed task-agnostic rubrics. Applying our framework to six families of LLM models whose propensities are incited in either direction, we find that we can measure how much the propensity is shifted and what effect this has on the tasks. Critically, propensities estimated using one benchmark successfully predict behaviour on held-out tasks. Moreover, we obtain stronger predictive power when combining propensities and capabilities than either separately. More broadly, our framework showcases how rigorous propensity measurements can be conducted and how it yields gains over solely using capability evaluations to predict AI behaviour.

