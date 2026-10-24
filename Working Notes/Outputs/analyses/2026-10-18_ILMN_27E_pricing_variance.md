# ILMN 2027E pricing variance to street (18 Oct 2026)

The table image is `Outputs/artifacts/2026-10-18_ILMN_27E_pricing_variance_table.png`. It is built by `scratchpad/variance_table.py`.

- **Street:** Bloomberg consensus, 10 Oct 2026.
- **Base case:** "Both legs".
- **Assumptions:** the street models 85% of a ~$100M-per-quarter conversion headwind. COGS and opex are held at street dollars. EPS uses an ~18% tax rate and 153M shares.

| 2027E | Street | Leg 1 only (−$60M) | Both legs (−$87M) | Like-for-like to 10% (−$126M) |
|---|---|---|---|---|
| Revenue | $4,918M | $4,858M | $4,831M | $4,792M |
| Δ to street | — | −$60M (−1.2%) | −$87M (−1.8%) | −$126M (−2.6%) |
| Revenue growth y/y | +6.3% | +5.0% | +4.5% | +3.6% |
| Δ to street | — | −130bps | −188bps | −272bps |
| Adj. gross margin | 69.05% | 68.7% | 68.5% | 68.2% |
| Δ to street | — | −38bps | −56bps | −81bps |
| Adj. operating margin | 25.2% | 24.3% | 23.9% | 23.3% |
| Δ to street | — | −92bps | −135bps | −197bps |
| Adj. EPS | $6.11 | ~$5.79 | ~$5.64 | ~$5.43 |
| Δ to street | — | −$0.32 (−5%) | −$0.47 (−8%) | −$0.68 (−11%) |

**1. Conversion headwind not in the street's numbers.** Taking the y/y change in Gb share and the y/y change in the 6000/X revenue-per-Gb ratio sizes the conversion headwind on consumables, net of pricing and volume. It was about 20%, then declined for three quarters to ~16%, where it has plateaued. That is ~$100M a quarter, or ~$400M a year. Management, the buy side and the sell side all expect it to subside. We hold it constant. Even if the street already models 85% of it, ~$60M is missing from 27E. That takes sequencing consumables growth to ~+6.9% from the street's +8.8% (~190bps) and revenue growth to ~+5.0% from +6.3% (~130bps).

**2. Like-for-like discounting steps up with the 35B.** Stripping out the conversion effect leaves ~8 points of like-for-like discounting. To reflect the 35B, we step that up by 10%, which is the step-up in discounting between the new 2027 flow cell and the prior high-volume flow cell. That takes like-for-like to ~8.8%, or another ~$27M. Combined, the two legs give ~$87M of downside: 27E sequencing consumables growth of ~+6.0% vs. +8.8% (~280bps) and revenue growth of ~+4.5% vs. +6.3% (~190bps). If like-for-like moves to 10% instead, the gap widens to ~$126M (~2.6% of revenue).

**3. Margins: the variance is pricing deleverage, not volume.** We aren't variant on volume growth, so we model COGS in line with the street in dollar terms. The same Gb ship at a lower price, so every dollar of the shortfall comes straight out of gross profit and operating income. Gross margin falls only ~55bps to ~68.5%, because revenue shrinks along with gross profit. Opex is also held at street, so the same $87M takes ~135bps off operating margin, to ~23.9% vs. 25.2%. EPS falls to ~$5.64, ~8% below the street's $6.11. At the 10% like-for-like case, operating margin is ~23.3%. That is below the FY26 guide of 23.4–23.6%, leaving 2027 EPS roughly flat on 2026.

## Version 2: like-for-like held at 8% (no 35B step-up)

Image: `Outputs/artifacts/2026-10-18_ILMN_27E_pricing_variance_table_lfl8.png`.

| 2027E | Street | Our 27E |
|---|---|---|
| Revenue | $4,918M | $4,858M (−$60M, −1.2%) |
| Revenue growth y/y | +6.3% | +5.0% (−130bps) |
| Seq. consumables revenue | $3,378M | $3,318M (−$60M, −1.8%) |
| Seq. consumables growth y/y | +8.8% | +6.9% (−193bps) |
| Adj. gross margin | 69.05% | 68.7% (−38bps) |
| Adj. operating margin | 25.2% | 24.3% (−92bps) |
| Adj. EPS | $6.11 | ~$5.79 (−$0.32, −5%) |

**1. Conversion headwind not in the street's numbers.** We size the conversion headwind from two inputs: the y/y change in Gb share and the y/y change in the 6000/X revenue-per-Gb ratio. That gives the headwind on consumables, net of pricing and volume. It was about 20%, declined for three quarters to ~16%, and has plateaued there. That is ~$100M a quarter, or ~$400M a year. Management, the buy side and the sell side all expect it to subside. We hold it constant. Even if the street already models 85% of it, ~$60M is missing from 27E. That takes sequencing consumables growth to ~+6.9% from the street's +8.8% (~190bps), and revenue growth to ~+5.0% from +6.3% (~130bps).

**2. Like-for-like discounting held at 8%, with no step-up.** Stripping out the conversion effect leaves ~8 points of like-for-like discounting. We hold that flat into 2027 and give no credit for the 35B being priced more aggressively than prior high-throughput flow cells. That is deliberately conservative. Each extra point of like-for-like discounting would add ~$33M of revenue downside, ~$0.18 of EPS and ~50bps of operating margin.

**3. Margins: pricing deleverage, not volume.** We aren't variant on volume growth, so we model COGS in line with the street in dollar terms. The same Gb ship at a lower price, so the $60M shortfall comes straight out of gross profit and operating income. Gross margin falls only ~40bps to ~68.7%, because revenue shrinks too. Opex is held at street, so operating margin falls ~90bps, to ~24.3% vs. 25.2%. EPS is ~$5.79, ~5% below the street's $6.11.

## Version 3: 2028E, with the 2027 assumptions carried forward

Image: `Outputs/artifacts/2026-10-18_ILMN_28E_pricing_variance_table.png`. Built by `scratchpad/variance_table_2028.py`.

**Method.**
- **Starting point:** our lower 2027 base.
- **Growth:** apply the street's 2028 sequencing consumables growth (+9.35%) to that base.
- **Headwind:** subtract another year of unmodeled headwind. That is ~$60M, the 15% of ~$400M a year the street doesn't model.
- **Held at street:** like-for-like discounting stays at 8%, and COGS and opex stay at street dollars.
- **Growth rates:** shown against our 2027E.

| 2028E | Street | Our 28E |
|---|---|---|
| Revenue | $5,263M | $5,137M (−$126M, −2.4%) |
| Revenue growth y/y | +7.0% | +5.7% (−126bps) |
| Seq. consumables revenue | $3,694M | $3,569M (−$126M, −3.4%) |
| Seq. consumables growth y/y | +9.3% | +7.5% (−181bps) |
| Adj. gross margin | 69.53% | 68.8% (−75bps) |
| Adj. operating margin | 26.5% | 24.7% (−180bps) |
| Adj. EPS | $7.01 | ~$6.34 (−$0.67, −10%) |

**The 2028 gap roughly doubles.**
- **Carried-over 2027 miss:** ~$60M, which grows to ~$66M at the street's growth rate.
- **New 2028 miss:** another ~$60M.

**Implications.**
- EPS growth: ours is ~+9.5% ($5.79 → $6.34), against the street's +14.7% ($6.11 → $7.01).
- Operating margin: ~24.7% vs. the street's 26.5%. That still misses management's ~26% 2027 target a year late.
