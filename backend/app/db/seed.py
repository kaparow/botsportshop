from decimal import Decimal

from sqlalchemy import select

from app.db.database import SessionLocal
from app.models.catalog import Category, Product


def run_seed() -> None:
    with SessionLocal() as db:
        existing = db.execute(select(Category.id)).first()
        if existing:
            print("Seed skipped: categories already exist")
            return

        sport = Category(name="Спортивное питание", slug="sportpit")
        supplements = Category(name="БАДы", slug="supplements")
        db.add_all([sport, supplements])
        db.flush()

        products = [
            Product(category_id=sport.id, name="Whey Protein 900g", slug="whey-protein-900", description="Сывороточный протеин для восстановления и роста.", price=Decimal("3490.00"), image_url="https://images.unsplash.com/photo-1579722821273-0f6c1f5a0f93?w=800"),
            Product(category_id=sport.id, name="Creatine Monohydrate 300g", slug="creatine-300", description="Креатин для силы и выносливости.", price=Decimal("1590.00"), image_url="https://images.unsplash.com/photo-1593095948071-474c5cc2989d?w=800"),
            Product(category_id=sport.id, name="BCAA 2:1:1", slug="bcaa-211", description="Аминокислоты для защиты мышц.", price=Decimal("1290.00"), image_url="https://images.unsplash.com/photo-1622483708347-2d4f87e5a2a5?w=800"),
            Product(category_id=sport.id, name="Pre-Workout Ignite", slug="preworkout-ignite", description="Предтрен для энергии и фокуса.", price=Decimal("1890.00"), image_url="https://images.unsplash.com/photo-1611078489935-0cb964de46d6?w=800"),
            Product(category_id=sport.id, name="Mass Gainer 3kg", slug="mass-gainer-3kg", description="Гейнер для набора массы.", price=Decimal("4290.00"), image_url="https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=800"),
            Product(category_id=supplements.id, name="Omega-3 1000mg", slug="omega3-1000", description="Поддержка сердца и сосудов.", price=Decimal("890.00"), image_url="https://images.unsplash.com/photo-1584367369853-50a0f9ca7ec0?w=800"),
            Product(category_id=supplements.id, name="Vitamin D3 + K2", slug="vitamin-d3-k2", description="Поддержка иммунитета и костей.", price=Decimal("990.00"), image_url="https://images.unsplash.com/photo-1607619056574-7b8d3ee536b2?w=800"),
            Product(category_id=supplements.id, name="Magnesium Chelate", slug="magnesium-chelate", description="Для восстановления нервной системы.", price=Decimal("1100.00"), image_url="https://images.unsplash.com/photo-1587854692152-cbe660dbde88?w=800"),
            Product(category_id=supplements.id, name="Zinc Picolinate", slug="zinc-picolinate", description="Поддержка гормонального баланса.", price=Decimal("740.00"), image_url="https://images.unsplash.com/photo-1550572017-edd951aa1be9?w=800"),
            Product(category_id=supplements.id, name="Multivitamin Daily", slug="multivitamin-daily", description="Комплекс витаминов на каждый день.", price=Decimal("1490.00"), image_url="https://images.unsplash.com/photo-1471864190281-a93a3070b6de?w=800"),
        ]
        db.add_all(products)
        db.commit()
        print("Seed completed")


if __name__ == "__main__":
    run_seed()
