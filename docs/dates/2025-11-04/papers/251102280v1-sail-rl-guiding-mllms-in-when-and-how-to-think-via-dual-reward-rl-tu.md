---
layout: default
title: SAIL-RL: Guiding MLLMs in When and How to Think via Dual-Reward RL Tuning
---

# SAIL-RL: Guiding MLLMs in When and How to Think via Dual-Reward RL Tuning
**arXiv**：[2511.02280v1](https://arxiv.org/abs/2511.02280) · [PDF](https://arxiv.org/pdf/2511.02280.pdf)  
**作者**：Fangxun Shu, Yongjie Ye, Yue Liao, Zijian Kang, Weijie Yin, Jiacong Wang, Xiao Liang, Shuicheng Yan, Chao Feng  

**一句话要点**：提出SAIL-RL强化学习框架，通过双奖励系统增强多模态大语言模型的推理能力。

**关键词**：强化学习调优, 多模态大语言模型, 推理能力增强, 双奖励系统, 幻觉减少, 自适应思考

## 3 点简述
- 现有方法仅监督结果，忽略推理质量，且思考策略单一。
- 采用双奖励系统：思考奖励评估推理质量，判断奖励自适应选择思考深度。
- 在SAIL-VL2模型上实验，提升推理与多模态理解，减少幻觉，性能媲美GPT-4o。

## 摘要（原文）

> We introduce SAIL-RL, a reinforcement learning (RL) post-training framework
> that enhances the reasoning capabilities of multimodal large language models
> (MLLMs) by teaching them when and how to think. Existing approaches are limited
> by outcome-only supervision, which rewards correct answers without ensuring
> sound reasoning, and by uniform thinking strategies, which often lead to
> overthinking on simple tasks and underthinking on complex ones. SAIL-RL
> addresses these challenges with a dual reward system: the Thinking Reward,
> which evaluates reasoning quality through factual grounding, logical coherence,
> and answer consistency, and the Judging Reward, which adaptively determines
> whether deep reasoning or direct answering is appropriate. Experiments on the
> state-of-the-art SAIL-VL2 show that SAIL-RL improves reasoning and multimodal
> understanding benchmarks at both 4B and 8B scales, achieving competitive
> performance against commercial closed-source models such as GPT-4o, and
> substantially reduces hallucinations, establishing it as a principled framework
> for building more reliable and adaptive MLLMs. The code will be available at
> https://github.com/BytedanceDouyinContent/SAIL-RL.

